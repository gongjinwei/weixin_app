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

    class Meta:
        model = models.SmallAppMenuStyle
        fields = '__all__'
