from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status
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


class ModelMappingViewsets(viewsets.ModelViewSet):
    queryset = models.ModelMapping.objects.all()
    serializer_class = serializers.ModelMappingSerializer


class ModelJoinViewsets(viewsets.ModelViewSet):
    queryset = models.ModelJoin.objects.all()
    serializer_class = serializers.ModelJoinSerializer


class TableSchemaViewsets(viewsets.ModelViewSet):
    queryset = models.TableSchema.objects.all()
    serializer_class = serializers.TableSchemaSerializer


class TableColumnViewsets(viewsets.ModelViewSet):
    queryset = models.TableColumn.objects.all()
    serializer_class = serializers.TableColumnSerializer


class MeasureViewsets(viewsets.ModelViewSet):
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


class CubeJoinViewsets(viewsets.ModelViewSet):
    queryset = models.CubeJoin.objects.all()
    serializer_class = serializers.CubeJoinSerializer


class CubeMappingViewsets(viewsets.ModelViewSet):
    queryset = models.CubeMapping.objects.all()
    serializer_class = serializers.CubeMappingSerializer


class HierarchyAttributeViewsets(viewsets.ModelViewSet):
    queryset = models.HierarchyAttribute.objects.all()
    serializer_class = serializers.HierarchyAttributeSerializer
