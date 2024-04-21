from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("phone_and_tabletProductadd",views.phone_and_tabletProductaddViewset)
router.register("PhoneAndTable",views.PhoneAndTableViewset)
router.register("productBrand",views.productBrandViewset)
router.register("ipadAndTAlet",views.ipadAndTABViewset)
router.register("specfication",views.specficationViewset)
router.register("Description",views.DescriptionViewset)


urlpatterns = [
  path("",include(router.urls))
]
