# -*- coding:UTF-8 -*-
from rest_framework import serializers

from . import models


class CreateSerializer(serializers.ModelSerializer):

    tmp_data = serializers.JSONField(help_text='只接收json',write_only=True)
    key = serializers.CharField(read_only=True)
    data = serializers.JSONField(read_only=True)

    class Meta:
        model = models.Create
        fields = '__all__'