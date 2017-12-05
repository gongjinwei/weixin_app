from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,status
from rest_framework.views import Response
from rest_framework.serializers import ValidationError
from rest_framework.decorators import list_route,detail_route
from . import models,serializers

from django_filters.rest_framework import DjangoFilterBackend

from collections import OrderedDict


class UserSmallAppMenusViewsets(viewsets.ModelViewSet):
    queryset = models.UserSmallAppMenus.objects.all()
    serializer_class = serializers.UserSmallAppMenusSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['parent_id']


class SmallAppMenuStyleViewsets(viewsets.ModelViewSet):
    queryset = models.SmallAppMenuStyle.objects.all()
    serializer_class = serializers.SmallAppMenuStyleSerializer





