# -*- coding:UTF-8 -*-

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('index',views.UserSmallAppMenusViewsets)
router.register('style',views.SmallAppMenuStyleViewsets)
router.register('config',views.CubesModelViewsets)
router.register('cubes',views.CubeViewsets)
router.register('dimensions',views.DimensionViewsets)
router.register('measures',views.MeasureViewsets)
router.register('aggregates',views.AggregateViewsets)
router.register('hierarchies',views.HierarchyViewsets)
router.register('dimensionLevels',views.DimensionLevelViewsets)
router.register('hierarchyLevels',views.HierarchyLevelViewsets)
router.register('dimensionAttributes',views.DimensionAttributeViewsets)
router.register('hierarchyAttributes',views.HierarchyAttributeViewsets)

urlpatterns = router.urls