from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status
import os
from configparser import ConfigParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Response
from rest_framework.serializers import ValidationError
from rest_framework.decorators import list_route, detail_route
from . import models, serializers

from django_filters.rest_framework import DjangoFilterBackend


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


class DimensionLevelViewsets(viewsets.ModelViewSet):
    """
        level用于数据库的GroupBy分组，attribute是维表中不用于GroupBy的属性
        有时level也可以带相关的attribute,例如level month：
        {
                 "name":"month",
                 "key": "month",
                 "label_attribute": "month_name",
                 "attributes": ["month", "month_name", "month_sname"]
        }
    """
    queryset = models.DimensionLevel.objects.all()
    serializer_class = serializers.DimensionLevelSerializer


class HierarchyLevelViewsets(viewsets.ModelViewSet):
    """
        level用于数据库的GroupBy分组，Hierarchy是对level的组合，
        有时level也可以带相关的attribute,例如level month：
        {
         "name":"month",
         "key": "month",
         "label_attribute": "month_name",
         "attributes": ["month", "month_name", "month_sname"]
        }
    """
    queryset = models.HierarchyLevel.objects.all()
    serializer_class = serializers.HierarchyLevelSerializer


class DimensionAttributeViewsets(viewsets.ModelViewSet):
    """
        attribute是维表中不用于GroupBy的属性，使用default_hierarchy
    """
    queryset = models.DimensionAttribute.objects.all()
    serializer_class = serializers.DimensionAttributeSerializer


class HierarchyAttributeViewsets(viewsets.ModelViewSet):
    """
        level用于数据库的GroupBy分组，attribute是维表中不用于GroupBy的属性
    """
    queryset = models.HierarchyAttribute.objects.all()
    serializer_class = serializers.HierarchyAttributeSerializer


class CubeDetailViewsets(viewsets.ModelViewSet):
    """
        用于引入立方体中非数量字段，引入后可作为量表的属性使用
    """
    queryset = models.CubeDetail.objects.all()
    serializer_class = serializers.CubeDetailSerializer


class SaveToModelFileViewsets(viewsets.ModelViewSet):
    """
        用于保存模型文件、触发服务配置文件更新与cube的重启
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


