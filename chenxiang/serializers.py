# -*- coding:UTF-8 -*-

from rest_framework import serializers
from . import models


class SaleSerializer(serializers.ModelSerializer):


    class Meta:
        model =models.Sale
        fields='__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Client
        fields='__all__'
