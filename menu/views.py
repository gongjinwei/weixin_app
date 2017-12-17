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


class DimensionViewsets(viewsets.ModelViewSet):
    queryset = models.Dimension.objects.all()
    serializer_class = serializers.DimensionSerializer


class MeasureViewsets(viewsets.ModelViewSet):
    """
        Measures are numerical properties of a fact. They might be represented, for example, as a table column
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
    queryset = models.DimensionLevel.objects.all()
    serializer_class = serializers.DimensionLevelSerializer


class HierarchyLevelViewsets(viewsets.ModelViewSet):
    queryset = models.HierarchyLevel.objects.all()
    serializer_class = serializers.HierarchyLevelSerializer


class DimensionAttributeViewsets(viewsets.ModelViewSet):
    queryset = models.DimensionAttribute.objects.all()
    serializer_class = serializers.DimensionAttributeSerializer


class HierarchyAttributeViewsets(viewsets.ModelViewSet):
    queryset = models.HierarchyAttribute.objects.all()
    serializer_class = serializers.HierarchyAttributeSerializer


class SaveToModelFileViewsets(viewsets.ModelViewSet):
    queryset = models.SaveToModelFile.objects.all()
    serializer_class = serializers.SaveToModelFileSerializer

    def perform_create(self, serializer):
        qs = serializer.validated_data['config']
        path = serializer.validated_data.get('path', r'/home/cks/HJ_Code/cubes_define')
        config_path = os.path.join(os.path.abspath(path), 'slicer.ini')
        if not os.path.isfile(config_path):
            raise ValidationError('%s不存在此配置文件' % config_path)
        name = qs.name
        model_path = os.path.join(path, '_models')
        configer = ConfigParser()
        if not os.path.exists(model_path):
            os.makedirs(model_path)
            configer.set('workspace', 'models_directory', model_path)
        config_serializer = serializers.CubesModelSerializer(qs)
        js = JSONRenderer().render(config_serializer.data)
        with open(os.path.join(model_path, name + '.json'), 'wb') as config_json:
            config_json.write(js)
        configer.read(config_path)
        configer.set('models', name, name + '.json')
        with open(config_path, 'w') as configfile:
            configer.write(configfile)
        serializer.save()
