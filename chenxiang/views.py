from django.shortcuts import render

# Create your views here.


from django.views.decorators.cache import cache_page
from rest_framework import viewsets,views

from . import serializers,models


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = models.Goods.objects.all()
    serializer_class = serializers.GoodsSerializer


class SaledtlViewSet(viewsets.ModelViewSet):
    queryset = models.Saledtl.objects.all()
    serializer_class = serializers.SaledtlSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer


class DeliverydtlViewSet(viewsets.ModelViewSet):
    queryset = models.Deliverydtl.objects.all()
    serializer_class = serializers.DeliverydtlSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = models.Operator.objects.all()
    serializer_class = serializers.OperatorSerializer




