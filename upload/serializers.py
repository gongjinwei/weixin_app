# -*- coding:UTF-8 -*-
from rest_framework import serializers

from . import models


class CreateSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(help_text='可接收字符串、数字、列表和json')

    class Meta:
        model = models.Create
        fields = '__all__'


class DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Create
        fields = ['dept_no','database_name','table_name','key_str']