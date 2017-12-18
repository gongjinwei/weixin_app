# -*- coding:UTF-8 -*-
from collections import OrderedDict
from rest_framework import serializers
from rest_framework.relations import PKOnlyObject
from rest_framework.fields import SkipField
from django.core.cache import cache

from . import models


class NotNullSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
                Object instance -> Dict of primitive datatypes.
                """
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is not None:
                if field.to_representation(attribute):
                    ret[field.field_name] = field.to_representation(attribute)

        return ret


class UserSmallAppMenusSerializer(serializers.ModelSerializer):
    category_id = serializers.ReadOnlyField(source='category_id.name')
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.UserSmallAppMenus
        fields = '__all__'

    def get_data(self, obj):
        record = cache.get(obj.company_api_name)
        return record


class SmallAppMenuStyleSerializer(serializers.ModelSerializer):
    script = serializers.JSONField()

    class Meta:
        model = models.SmallAppMenuStyle
        fields = '__all__'


class MeasureSerializer(NotNullSerializer):
    class Meta:
        model = models.Measure
        fields = '__all__'


class CubeJoinSerializer(NotNullSerializer):
    cube = serializers.SlugRelatedField(slug_field='id', write_only=True, queryset=models.Cube.objects.all())

    class Meta:
        model = models.CubeJoin
        fields = '__all__'


class AggregateSerializer(NotNullSerializer):
    cube = serializers.SlugRelatedField(slug_field='id', queryset=models.Cube.objects.all(), write_only=True)

    class Meta:
        model = models.Aggregate
        fields = '__all__'


class DimensionLevelSerializer(NotNullSerializer):
    class Meta:
        model = models.DimensionLevel
        fields = '__all__'


class HierarchyLevelSerializer(NotNullSerializer):

    class Meta:
        model = models.HierarchyLevel
        fields = '__all__'


class DimensionAttributeSerializer(NotNullSerializer):
    dimension = serializers.SlugRelatedField(slug_field='id', queryset=models.Dimension.objects.all(),
                                             write_only=True)

    class Meta:
        model = models.DimensionAttribute
        fields = '__all__'


class HierarchyAttributeSerializer(NotNullSerializer):
    class Meta:
        model = models.HierarchyAttribute
        fields = '__all__'


class HierarchySerializer(NotNullSerializer):
    levels = serializers.StringRelatedField(many=True, read_only=True)
    dimension = serializers.SlugRelatedField(slug_field='id', queryset=models.Dimension.objects.all(),
                                             write_only=True)

    class Meta:
        model = models.Hierarchy
        fields = '__all__'


class DimensionSerializer(NotNullSerializer):
    levels = serializers.StringRelatedField(many=True)
    hierarchies = HierarchySerializer(many=True, read_only=True)
    attributes = DimensionAttributeSerializer(many=True, read_only=True)
    model = serializers.SlugRelatedField(slug_field='id', queryset=models.CubesModel.objects.all(), write_only=True)

    class Meta:
        model = models.Dimension
        fields = '__all__'


class CubeDetailSerializer(NotNullSerializer):
    cube = serializers.SlugRelatedField(slug_field='id', write_only=True, queryset=models.Cube.objects.all())

    class Meta:
        model = models.CubeDetail
        fields = '__all__'


class CubeSerializer(NotNullSerializer):
    dimensions = serializers.SlugRelatedField(slug_field='name', many=True, queryset=models.Dimension.objects.all())
    measures = serializers.StringRelatedField(many=True)
    model = serializers.SlugRelatedField(slug_field='id', queryset=models.CubesModel.objects.all(), write_only=True)
    aggregates = AggregateSerializer(many=True, read_only=True)
    mappings = serializers.JSONField(allow_null=True,
                                     help_text='所使用属性与物理表属性的对应关系，例如："mappings": {"year":"sales_year","amount":"total_amount"]}（可选）')
    joins = CubeJoinSerializer(many=True, read_only=True)
    details = CubeDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Cube
        fields = '__all__'


class CubesModelSerializer(NotNullSerializer):
    cubes = CubeSerializer(many=True, read_only=True)
    dimensions = DimensionSerializer(many=True, read_only=True)
    mappings = serializers.JSONField(allow_null=True, help_text='model级别的对应关系，可被cube的mappings继承，接收json输入（可选）')
    joins = serializers.JSONField(allow_null=True, help_text='model级别连接关系，可被cube的joins继承，接收json输入（可选）')

    class Meta:
        model = models.CubesModel
        fields = '__all__'


class SaveToModelFileSerializer(NotNullSerializer):
    class Meta:
        model = models.SaveToModelFile
        fields = '__all__'
