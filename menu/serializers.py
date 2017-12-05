# -*- coding:UTF-8 -*-
from rest_framework import serializers

from . import models


class UserSmallAppMenusSerializer(serializers.ModelSerializer):
    category_id = serializers.ReadOnlyField(source='category_id.name')

    class Meta:
        model = models.UserSmallAppMenus
        fields = '__all__'


class SmallAppMenuStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SmallAppMenuStyle
        fields = '__all__'
