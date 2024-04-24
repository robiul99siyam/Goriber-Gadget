from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("fitnessAndwearable",views.fitnessAndWearableViewset)
router.register("watachAndaccessories",views.watachAndaccessoriesViewset)
router.register("FitnessDescription",views.FitnessDescriptionViewsets)
router.register("FitnessSpecfication",views.FitnessSpecficationViewset)
router.register("Fitness_and_wearable_Product",views.Fitness_and_wearable_ProductViewset)

urlpatterns = [
  path("",include(router.urls))
]
