# -*- coding:UTF-8 -*-
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sale', views.SaleViewSet)
router.register(r'client', views.ClientViewSet)
urlpatterns = router.urls