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
