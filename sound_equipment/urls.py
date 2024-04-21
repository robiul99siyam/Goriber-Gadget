from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("sound/equipment",views.speckerViewset)
router.register("speacker",views.soundSpeckerProductAddViewset)
router.register("add/product/all",views.SoundAndEquipmentViewset)
router.register("SoundSpecification",views.SoundSpecificationViewsets)
router.register("SoundDescription",views.SoundDescriptionViewsets)


urlpatterns = [
  path("",include(router.urls))
]
