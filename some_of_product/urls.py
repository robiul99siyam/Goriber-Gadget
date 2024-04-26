from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("benner",views.BennerViewset)
router.register("featureProduct",views.featureProductViewset)
router.register("featureCategroy",views.FeaturedCategoryViewset)
router.register("ReadyOnorder",views.ReadyofOrderViewset)

urlpatterns = [
  
  path("",include(router.urls))
]

