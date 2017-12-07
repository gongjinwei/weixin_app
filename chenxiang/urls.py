# -*- coding:UTF-8 -*-
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sale', views.SaleViewSet)
router.register(r'saledtl', views.SaledtlViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'goods', views.GoodsViewSet)
router.register(r'purchase', views.PurchaseViewSet)
router.register(r'shop', views.ShopViewSet)
urlpatterns = router.urls