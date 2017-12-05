from django.shortcuts import render

# Create your views here.


from django.views.decorators.cache import cache_page
from rest_framework import viewsets,views

from . import serializers,models


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer




