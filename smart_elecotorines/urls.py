from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("smart_elecotorinesProductAdd",views. smart_elecotorinesProductAddViewsets)
router.register("product/brand",views.ProductBrandViewsets)
router.register("mediaAndStreams",views.mediaAndStreamsViewsets)
router.register("smartAndelectines",views.smartAndelectinesViewsets)
router.register("smartSpecification",views.SmartSpecificationViewsets)
router.register("smartDescription",views.SmartDescription)


urlpatterns = [
  path("",include(router.urls))
]
