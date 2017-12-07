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


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Goods
        fields='__all__'


class SaledtlSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Saledtl
        fields='__all__'


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Purchase
        fields='__all__'


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Shop
        fields='__all__'


class SaleorderSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Saleorder
        fields='__all__'
