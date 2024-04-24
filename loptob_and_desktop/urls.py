from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("ultraBook",views.ultraBookViewsets)
router.register("laptob/prodcut/barnad",views.ProductBrandViewsets)
router.register("BussinessClassLoptob",views.BusineesClassLoptobViewsets)
router.register("GamingLaptob",views.GamingLaptobViewsets)
router.register('laptobAndDestopAdd',views.laptob_and_destop_productAddViewsets)
router.register('LaptobSpecfication',views.LaptobSpecifationViewset)
router.register('LaptobDescription',views.LaptobDescriptionViewset)



urlpatterns = [
  path("",include(router.urls))
]
