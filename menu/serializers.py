# -*- coding:UTF-8 -*-
from rest_framework import serializers
from django.core.cache import cache

from . import models


class UserSmallAppMenusSerializer(serializers.ModelSerializer):
    category_id = serializers.ReadOnlyField(source='category_id.name')
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.UserSmallAppMenus
        fields = '__all__'

    def get_data(self,obj):
        record=cache.get(obj.company_api_name)
        return record


class SmallAppMenuStyleSerializer(serializers.ModelSerializer):
    script = serializers.JSONField()

    class Meta:
        model = models.SmallAppMenuStyle
        fields = '__all__'


class DimensionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dimension
        fields = '__all__'


class HierarchySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hierarchy
        fields = '__all__'


class MeasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Measure
        fields = '__all__'


class AggregateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Aggregate
        fields = '__all__'


class CubeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cube
        fields = '__all__'


class TableColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TableColumn
        fields = '__all__'


class TableSchemaSerializer(serializers.ModelSerializer):
    column = TableColumnSerializer(many=True,read_only=True)

    class Meta:
        model = models.TableSchema
        fields = '__all__'


class ModelMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ModelMapping
        fields = '__all__'


class CubeMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CubeMapping
        fields = '__all__'


class DimensionLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DimensionLevel
        fields = '__all__'


class HierarchyLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HierarchyLevel
        fields = '__all__'


class DimensionAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DimensionAttribute
        fields = '__all__'


class HierarchyAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HierarchyAttribute
        fields = '__all__'


class ModelJoinSerializer(serializers.ModelSerializer):
    master = TableSchemaSerializer(read_only=True)

    class Meta:
        model = models.ModelJoin
        fields = '__all__'


class CubeJoinSerializer(serializers.ModelSerializer):
    master = TableSchemaSerializer(read_only=True)

    class Meta:
        model = models.CubeJoin
        fields = '__all__'


class CubesModelSerializer(serializers.ModelSerializer):
    cubes = CubeSerializer(many=True,read_only=True)
    dimensions = DimensionSerializer(many=True,read_only=True)
    mappings = ModelMappingSerializer(many=True,read_only=True)
    joins = ModelJoinSerializer(many=True,read_only=True)

    class Meta:
        model = models.CubesModel
        fields = '__all__'
