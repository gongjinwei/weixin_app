from django.shortcuts import render

# Create your views here.
import os, datetime
from configparser import ConfigParser

from django.conf import settings
from rest_framework import viewsets, filters, status
from rest_framework.serializers import ValidationError
from rest_framework.decorators import list_route, detail_route

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.views import Response, status

from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers

DatabaseFormat = {
    '1': 'mssql+pyodbc://{}?driver=SQL+Server+Native+Client+11.0',
    '2': 'mssql+pymssql://{}',
    '3': 'mysql+mysqldb://{}?charset=utf8'
}


class CreateOnlyViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    A viewset that provides default `create()` actions.
    """
    pass


class ObtainExpireAuthToken(ObtainAuthToken, CreateOnlyViewSet):
    """"
        输入用户名和密码来获取Token,请求头带上Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
    """

    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            time_now = datetime.datetime.now()
            EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)
            if created or token.created < time_now - datetime.timedelta(minutes=EXPIRE_MINUTES):
                token.delete()
                token = Token.objects.create(user=user)
                token.created = time_now
                token.save()
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSmallAppMenusViewsets(viewsets.ModelViewSet):
    queryset = models.UserSmallAppMenus.objects.all()
    serializer_class = serializers.UserSmallAppMenusSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['parent_id']


class SmallAppMenuStyleViewsets(viewsets.ModelViewSet):
    queryset = models.SmallAppMenuStyle.objects.all()
    serializer_class = serializers.SmallAppMenuStyleSerializer


class CubesModelViewsets(viewsets.ModelViewSet):
    queryset = models.CubesModel.objects.all()
    serializer_class = serializers.CubesModelSerializer


class CubeViewsets(viewsets.ModelViewSet):
    queryset = models.Cube.objects.all()
    serializer_class = serializers.CubeSerializer


class CubeJoinViewsets(viewsets.ModelViewSet):
    """
        用于建立量表与维表之间的关联，建立关联后，才可以引入维表字段。为常用功能。
    """
    queryset = models.CubeJoin.objects.all()
    serializer_class = serializers.CubeJoinSerializer


class DimensionViewsets(viewsets.ModelViewSet):
    queryset = models.Dimension.objects.all()
    serializer_class = serializers.DimensionSerializer


class MeasureViewsets(viewsets.ModelViewSet):
    """
        度量，是量表的数量属性，常表现为一个表的字段。
    """
    queryset = models.Measure.objects.all()
    serializer_class = serializers.MeasureSerializer


class AggregateViewsets(viewsets.ModelViewSet):
    queryset = models.Aggregate.objects.all()
    serializer_class = serializers.AggregateSerializer


class HierarchyViewsets(viewsets.ModelViewSet):
    queryset = models.Hierarchy.objects.all()
    serializer_class = serializers.HierarchySerializer


class LevelViewsets(viewsets.ModelViewSet):
    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer


class AttributeViewsets(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer


class CubeDetailViewsets(viewsets.ModelViewSet):
    """
        用于引入立方体中非数量字段，引入后可作为量表的属性使用
    """
    queryset = models.CubeDetail.objects.all()
    serializer_class = serializers.CubeDetailSerializer


class SaveToModelFileViewsets(viewsets.ModelViewSet):
    """
        用于保存/删除模型文件、修改操作均触发服务配置文件的更新与重启
    """
    queryset = models.SaveToModelFile.objects.all()
    serializer_class = serializers.SaveToModelFileSerializer

    def perform_create(self, serializer):
        qs = serializer.validated_data['config']
        path = serializer.validated_data.get('path', r'/www/wwwroot/cubes_define')
        config_path = os.path.join(os.path.abspath(path), 'slicer.ini')
        if not os.path.isfile(config_path):
            raise ValidationError('不存在此配置文件:%s' % config_path)
        name = qs.name
        model_path = os.path.join(path, '_models')
        configer = ConfigParser()
        if not os.path.exists(model_path):
            os.makedirs(model_path)
            configer.set('workspace', 'models_directory', model_path)
        config_serializer = serializers.CubesModelSerializer(qs)
        js = JSONRenderer().render(config_serializer.data)  # 序列化出所需要的JSON数据
        with open(os.path.join(model_path, name + '.json'), 'wb') as config_json:
            config_json.write(js)
        configer.read(config_path)
        configer.set('models', name, name + '.json')
        with open(config_path, 'w') as configfile:
            configer.write(configfile)
        serializer.save()

    def perform_update(self, serializer):
        qs = serializer.validated_data['config']
        path = serializer.validated_data['path']
        config_path = os.path.join(os.path.dirname(os.path.dirname(path)), 'slicer.ini')
        config_serializer = serializers.CubesModelSerializer(qs)
        js = JSONRenderer().render(config_serializer.data)
        with open(path, 'wb') as config_json:
            config_json.write(js)
        configer = ConfigParser()
        configer.read(config_path)
        with open(config_path, 'w') as configfile:
            configer.write(configfile)
        serializer.save()

    def perform_destroy(self, instance):
        try:
            os.remove(instance.path)
        except OSError:
            pass
        config_path = os.path.join(os.path.dirname(os.path.dirname(instance.path)), 'slicer.ini')
        config = ConfigParser()
        config.read(config_path)
        config.remove_option('models', instance.config.name)
        with open(config_path, 'w') as configfile:
            config.write(configfile)
        instance.delete()
