from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("Peripheries",views.PeripheriesViewsets)
router.register("Product",views.peripheriesProudctViewsets)

# router.register("laptob_and_destop_productAdd",views.laptob_and_destop_productAdd)

urlpatterns = [
  path("",include(router.urls))
]
