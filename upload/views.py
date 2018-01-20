from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, exceptions
from rest_framework.views import Response, status
from rest_framework.decorators import list_route
from kazoo.client import KazooClient
import hashlib


from . import serializers, models, tasks
from utils.viewsets import CreateListViewSet

# hosts = getattr(settings, 'KAZOO_CLIENTS', '127.0.0.1:2181')
# zk = KazooClient(hosts=hosts)


# Create your views here.

def create_md5(request_data, key):
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
            _data = serializer.validated_data.pop('tmp_data', None)
            if not isinstance(_data, dict):
                raise exceptions.ValidationError('data must be a json')
            # 如果传入的json数据不为空，则对data进行解析
            if _data:
                # 收集正确列表
                success_list = []
                # 收集错误列表
                failure_list = []
                for k, v in _data.items():
                    try:
                        # 如果成功新建实例则返回序列化对象，否则返回错误列表
                        m_id = create_md5(request.data, k)
                        # 判断是否存在实例，如果存在则更新，否则新建
                        _serializer = serializers.CreateFinalSerializer(data=dict(data=v))
                        if _serializer.is_valid(raise_exception=True):
                            obj, created = models.Create.objects.update_or_create(
                                defaults=dict(key=k, **serializer.validated_data, **_serializer.data), id=m_id)
                            # 最后将结果序列化到前端
                            success_list.append(serializers.CreateListSerializer(obj).data)
                    except:
                        failure_list.append(dict(dept_no=serializer.validated_data['dept_no'],
                                                 database_name=serializer.validated_data['database_name'],
                                                 table_name=serializer.validated_data['table_name'],key=k))
                # 取出最新的更新时间
                return Response({"success": success_list, "failure": failure_list})
            return Response("data can't be null", status=status.HTTP_400_BAD_REQUEST)
