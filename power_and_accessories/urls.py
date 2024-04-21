from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("PowerAndAccessries",views.powerAndaccessoriesViewset)
router.register("productBrand",views.productBrandViewset)
router.register("cableAndInternConnectProductAdd",views.cableAndInternConnectProductAddviewset)
router.register("owerAndaccessoriesDescription",views.powerAndaccessoriesDescriptionViewsets)
router.register("PowerAndaccessoriesSpecificaion",views.PowerAndaccessoriesSpecificaionViewsets)


urlpatterns = [
  path("",include(router.urls))
]
