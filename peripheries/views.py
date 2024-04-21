from django.shortcuts import render
from .serializer import peripheriesProductSerializer,PeriperiesSerializer
from .models import peripheriesProduct,Perpheries
from rest_framework import viewsets
from rest_framework import filters
from conver_and_glass.views import All_pagination
from django.http import Http404
class PeripheriesViewsets(viewsets.ModelViewSet):
    queryset = Perpheries.objects.all()
    serializer_class = PeriperiesSerializer
    
    
class peripheriesProudctViewsets(viewsets.ModelViewSet):
    queryset = peripheriesProduct.objects.all()
    serializer_class =  peripheriesProductSerializer
    pagination_class = All_pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["Perpheries__name","ProductBrand__name",'name']

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return peripheriesProduct.objects.filter(id=params_id)
            except peripheriesProduct.DoesNotExist:
                return Http404("periphers  does not exist for the given params_id")
        return peripheriesProduct.objects.all()
    