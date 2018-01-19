# -*- coding:UTF-8 -*-
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()

router.register('index',views.CreateViewSets)

urlpatterns = router.urls

