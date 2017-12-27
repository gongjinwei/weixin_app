from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.views import Response, status
from kazoo.client import KazooClient

from . import serializers, models, tasks

zk = KazooClient(hosts='192.168.31.71:2181,192.168.31.72:2181,192.168.31.73:2181')


# Create your views here.


class CreateViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.CreateSerializer
    queryset = models.Create.objects.all()

    def create(self, request, *args, **kwargs):
        zk.start()

        if request.data['last_version'] == -1:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            create_path = '/'.join(
                ['', serializer.validated_data['dept_no'], serializer.validated_data['database_name'],
                 serializer.validated_data['table_name'], serializer.validated_data['key_str']])
            zk.ensure_path(create_path)
            data, stat = zk.get(create_path)

            zk.stop()
            serializer.save(version=stat.version)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            if not self.queryset.filter(pk=request.data['id']).exists():
                raise exceptions.ValidationError('你的版本号不正确')
            instance = self.queryset.get(pk=request.data['id'])
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            create_path = '/'.join(
                ['', serializer.validated_data['dept_no'], serializer.validated_data['database_name'],
                 serializer.validated_data['table_name'], serializer.validated_data['key_str']])
            transaction = zk.transaction()
            transaction.check(create_path, version=serializer.validated_data['last_version'])
            zk.ensure_path(create_path)
            results = transaction.commit()
            data, stat = zk.get(create_path)
            zk.stop()
            if True in results:

                serializer.save(version=stat.version)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response(serializer.data)
            else:
                raise exceptions.ValidationError('你的版本号不正确')
