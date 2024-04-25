from django.shortcuts import render
from .models import powerAndaccessories,PowerProductBrand,cableAndinternconnectProductAdd,powerAndaccessoriesDescriptionModel,PowerAndaccessoriesSpecificaionModel,cableAndinternconnect
from .serializer import powerAndaccessrorieSerailzer,productBrandSerailzer,cableAndinternconnectProductAddSerailzer,powerAndaccessoriesDescriptionSerailzer,PowerAndaccessoriesSpecificaionSerializer
from rest_framework import filters
from conver_and_glass.views import All_pagination
from rest_framework import viewsets
from django.http import Http404

class powerAndaccessoriesDescriptionViewsets(viewsets.ModelViewSet):
    queryset = powerAndaccessoriesDescriptionModel.objects.all()
    serializer_class = powerAndaccessoriesDescriptionSerailzer

class PowerAndaccessoriesSpecificaionViewsets(viewsets.ModelViewSet):
    queryset = PowerAndaccessoriesSpecificaionModel.objects.all()
    serializer_class = PowerAndaccessoriesSpecificaionSerializer


class powerAndaccessoriesViewset(viewsets.ModelViewSet):
    queryset = powerAndaccessories.objects.all()
    serializer_class = powerAndaccessrorieSerailzer


class productBrandViewset(viewsets.ModelViewSet):
    queryset = PowerProductBrand.objects.all()
    serializer_class = productBrandSerailzer

class cableAndInternConnectProductAddviewset(viewsets.ModelViewSet):
    queryset = cableAndinternconnectProductAdd.objects.all()
    serializer_class = cableAndinternconnectProductAddSerailzer
    pagination_class = All_pagination
    filter_backends  = [filters.SearchFilter]
    search_fields = ["powerAndaccessories__name","cableAndinternconnect__name","productBrand__name","name"]


    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return cableAndinternconnectProductAdd.objects.filter(id=params_id)
            except cableAndinternconnectProductAdd.DoesNotExist:
                return Http404("cable and interconnect does not exist for the given params_id")
        return cableAndinternconnectProductAdd.objects.all()