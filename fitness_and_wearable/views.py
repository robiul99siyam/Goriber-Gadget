from django.shortcuts import render
from .models import fitnessAndwearable,Fitness_and_wearable_Product,watachAndaccessories,FitnessDescriptionModel,FitnessSpecificaionModel

from .serializer import fitnessAndwearableSerializers,Fitness_and_wearable_ProductSerializers,watachAndaccessoriesSerializers,FitnessDescriptionSerializer,FitnessSpceificationSerailzer
from rest_framework import viewsets
from rest_framework import filters
# from conver_and_glass.views import All_pagination
from django.http import Http404

class fitnessAndWearableViewset (viewsets.ModelViewSet):
    queryset = fitnessAndwearable.objects.all()
    serializer_class = fitnessAndwearableSerializers

class watachAndaccessoriesViewset (viewsets.ModelViewSet):
    queryset = watachAndaccessories.objects.all()
    serializer_class = watachAndaccessoriesSerializers


class FitnessDescriptionViewsets(viewsets.ModelViewSet):
    queryset = FitnessDescriptionModel.objects.all()
    serializer_class = FitnessDescriptionSerializer

class Fitness_and_wearable_ProductViewset (viewsets.ModelViewSet):
    queryset = Fitness_and_wearable_Product.objects.all()
    serializer_class = Fitness_and_wearable_ProductSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['productBrand__name', 'fitnessAndwearable__name,watachAndaccessories__name']
    # pagination_class = All_pagination

    def get_queryset(self):
        params_id = self.request.query_params.get("query_params")

        if params_id is not None:
            try:
                return Fitness_and_wearable_Product.objects.filter(id=params_id)
            except Fitness_and_wearable_Product.DoesNotExist:
                raise Http404("Fitness Product does not exist for the given params_id ")
        return Fitness_and_wearable_Product.objects.all()
