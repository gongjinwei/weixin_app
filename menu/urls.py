# -*- coding:UTF-8 -*-

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('index',views.UserSmallAppMenusViewsets)
router.register('style',views.SmallAppMenuStyleViewsets)
router.register('models',views.CubesModelViewsets)
router.register('cubes',views.CubeViewsets)
router.register('measures',views.MeasureViewsets)
router.register('cubeDetails',views.CubeDetailViewsets)
router.register('aggregates',views.AggregateViewsets)
router.register('cubeJoin',views.CubeJoinViewsets)
router.register('dimensions',views.DimensionViewsets)
router.register('hierarchies',views.HierarchyViewsets)
router.register('levels',views.LevelViewsets)
router.register('attributes',views.AttributeViewsets)
router.register('configFiles',views.SaveToModelFileViewsets)

urlpatterns = router.urls