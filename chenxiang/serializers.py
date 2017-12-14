# -*- coding:UTF-8 -*-

from rest_framework import serializers
from . import models


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Shop
        fields='__all__'

class OperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Operator
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
    goods=GoodsSerializer(read_only=True)

    class Meta:
        model =models.Saledtl
        fields='__all__'


class SaleSerializer(serializers.ModelSerializer):
    shop=ShopSerializer(read_only=True)
    operator=OperatorSerializer(read_only=True)
    details = SaledtlSerializer(many=True,read_only=True)

    class Meta:
        model =models.Sale
        fields='__all__'


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Purchase
        fields='__all__'


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Delivery
        fields='__all__'


class DeliverydtlSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Deliverydtl
        fields='__all__'
