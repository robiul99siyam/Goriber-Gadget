from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("coverGlass",views.coverGlassViewset)
router.register("cover/product/brand",views.ProductViewset)
router.register("cover/product/add",views.CoverAndGlassProductAdd)


urlpatterns = [
  path("",include(router.urls))
]
