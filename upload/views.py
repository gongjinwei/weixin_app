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

def create_md5(request_data,key):
    if key:
        m = hashlib.md5()
        m.update(request_data.get('dept_no', '').encode())
        m.update(request_data.get('database_name', '').encode())
        m.update(request_data.get('table_name', '').encode())
        m.update(key.encode())
        return m.hexdigest()


class CreateViewSets(CreateListViewSet):
    serializer_class = serializers.CreateSerializer
    queryset = models.Create.objects.all()

    def create(self, request, *args, **kwargs):
        # 首先对数据进行验证
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 输入验证后再进行所需类型的验证
            _data = serializer.validated_data.pop('tmp_data',None)
            if not isinstance(_data,dict):
                raise exceptions.ValidationError('data must be a json')
            # 如果传入的json数据不为空，则对data进行解析
            if _data:

                for k,v in _data.items():
                    m_id = create_md5(request.data,k)
                    obj,created = models.Create.objects.get_or_create(id=m_id)

                    for key,value in dict(data=v,**serializer.validated_data,key=k).items():
                        setattr(obj,key,value)
                    obj.save()
                # 取出最新的更新时间
                return Response('OK')
            return Response("data can't be null",status=status.HTTP_400_BAD_REQUEST)

