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
        exclude = ['id']


class AggregateSerializer(NotNullSerializer):
    measure = serializers.SlugRelatedField(slug_field='name', queryset=models.Measure.objects.all(), allow_null=True)
    cube = serializers.SlugRelatedField(slug_field='name', queryset=models.Cube.objects.all(), write_only=True)

    class Meta:
        model = models.Aggregate
        exclude = ['id']


class DimensionLevelSerializer(NotNullSerializer):
    class Meta:
        model = models.DimensionLevel
        exclude = ['id']


class HierarchyLevelSerializer(NotNullSerializer):
    class Meta:
        model = models.HierarchyLevel
        exclude = ['id']


class DimensionAttributeSerializer(NotNullSerializer):
    dimension = serializers.SlugRelatedField(slug_field='name', queryset=models.Dimension.objects.all(),
                                             write_only=True)

    class Meta:
        model = models.DimensionAttribute
        exclude = ['id']


class HierarchyAttributeSerializer(NotNullSerializer):
    class Meta:
        model = models.HierarchyAttribute
        exclude = ['id']


class HierarchySerializer(NotNullSerializer):
    levels = serializers.StringRelatedField(many=True, read_only=True)
    dimension = serializers.SlugRelatedField(slug_field='name', queryset=models.Dimension.objects.all(),
                                             write_only=True)

    class Meta:
        model = models.Hierarchy
        exclude = ['id']


class DimensionSerializer(NotNullSerializer):
    levels = serializers.StringRelatedField(many=True, read_only=True)
    hierarchies = HierarchySerializer(many=True, read_only=True)
    attributes = DimensionAttributeSerializer(many=True, read_only=True)
    model = serializers.SlugRelatedField(slug_field='name', queryset=models.CubesModel.objects.all(), write_only=True)

    class Meta:
        model = models.Dimension
        exclude = ['id']


class CubeSerializer(NotNullSerializer):
    dimensions = serializers.SlugRelatedField(slug_field='name', many=True, queryset=models.Dimension.objects.all())
    measures = serializers.SlugRelatedField(slug_field='name', many=True, queryset=models.Measure.objects.all())
    model = serializers.SlugRelatedField(slug_field='name', queryset=models.CubesModel.objects.all(), write_only=True)
    aggregates = AggregateSerializer(many=True, read_only=True)
    mappings = serializers.JSONField(allow_null=True,help_text='对应关系（可选）')
    joins = serializers.JSONField(allow_null=True, help_text='连接关系（可选）')

    class Meta:
        model = models.Cube
        exclude = ['id']


class CubesModelSerializer(NotNullSerializer):
    cubes = CubeSerializer(many=True, read_only=True)
    dimensions = DimensionSerializer(many=True, read_only=True)
    mappings = serializers.JSONField(allow_null=True, help_text='对应关系（可选）')
    joins = serializers.JSONField(allow_null=True, help_text='连接关系（可选）')

    class Meta:
        model = models.CubesModel
        exclude = ['id']
