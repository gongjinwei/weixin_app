from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, exceptions
from rest_framework.views import Response, status
from rest_framework.decorators import list_route
from kazoo.client import KazooClient
import hashlib

from . import serializers, models, tasks
from utils.viewsets import CreateListViewSet

hosts = getattr(settings, 'KAZOO_CLIENTS', '127.0.0.1:2181')
zk = KazooClient(hosts=hosts)


# Create your views here.

def create_md5(request_data):
    m = hashlib.md5()
    m.update(request_data.get('dept_no', '').encode())
    m.update(request_data.get('database_name', '').encode())
    m.update(request_data.get('table_name', '').encode())
    m.update(request_data.get('key_str', '').encode())
    return m.hexdigest()


class CreateViewsets(CreateListViewSet):
    serializer_class = serializers.CreateSerializer
    queryset = models.Create.objects.all()

    def create(self, request, *args, **kwargs):
        m_id = create_md5(request.data)
        last_version = int(request.data.get('last_version', 0))
        zk.start()

        if not self.queryset.filter(pk=m_id).exists():
            if last_version != -1:
                raise exceptions.ValidationError('last_version must be -1 when you want to create')
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            create_path = '/'.join(
                ['', serializer.validated_data['dept_no'], serializer.validated_data['database_name'],
                 serializer.validated_data['table_name'], serializer.validated_data['key_str']])
            zk.ensure_path(create_path)
            data_s = '%s:%s' % (m_id, -1)
            zk.set(create_path, data_s.encode())
            zk.stop()
            serializer.save(version=0, id=m_id)
            headers = self.get_success_headers(serializer.data)
            return Response({'current_version': 0}, status=status.HTTP_201_CREATED, headers=headers)
        elif last_version > -1:
            instance = self.queryset.get(pk=m_id)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            create_path = '/'.join(
                ['', serializer.validated_data['dept_no'], serializer.validated_data['database_name'],
                 serializer.validated_data['table_name'], serializer.validated_data['key_str']])
            transaction = zk.transaction()
            transaction.check(create_path, version=last_version)
            zk.ensure_path(create_path)
            data_s = '%s:%s' % (m_id, last_version)
            transaction.set_data(create_path, data_s.encode())
            results = transaction.commit()

            if True in results:
                data, stat = zk.get(create_path)
                zk.stop()
                serializer.save(version=stat.version)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response({'current_version': stat.version})
            else:
                zk.stop()
                raise exceptions.ValidationError('You should update first before you submit a new one')
        else:
            raise exceptions.ValidationError('This record had been created . Last_version should set greater than -1')

    @list_route(methods=['post'], serializer_class=serializers.DeleteSerializer)
    def delete(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        m_id = create_md5(serializer.validated_data)

        if self.queryset.filter(pk=m_id).exists():

            instance = self.queryset.get(pk=m_id)
            instance.delete()
            delete_path = '/'.join(
                ['', serializer.validated_data['dept_no'], serializer.validated_data['database_name'],
                 serializer.validated_data['table_name'], serializer.validated_data['key_str']])
            zk.start()
            zk.delete(delete_path)
            zk.stop()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise exceptions.NotFound('This obj does not exist')
