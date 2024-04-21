from django.shortcuts import render
from .models import phone_and_tabletProductadd,phoneAndtablet,productBrand,ipadAndTAB,SpecificationModel,DescriptionModel
from .serializer import phone_and_tabletProductaddSerilizer,PhoneAndtabletSerializer,ipadAndTabSerilizer,ProductBrandSerilizer,specficationSerailzer,DescriptionSerializer

from rest_framework import viewsets
from rest_framework import filters
from conver_and_glass.views import All_pagination
from django.http import Http404


class PhoneAndTableViewset(viewsets.ModelViewSet):
    queryset = phoneAndtablet.objects.all()
    serializer_class = PhoneAndtabletSerializer


class productBrandViewset(viewsets.ModelViewSet):
    queryset = productBrand.objects.all()
    serializer_class = ProductBrandSerilizer

class ipadAndTABViewset(viewsets.ModelViewSet):
    queryset = ipadAndTAB.objects.all()
    serializer_class = ipadAndTabSerilizer


class specficationViewset(viewsets.ModelViewSet):
    queryset = SpecificationModel.objects.all()
    serializer_class = specficationSerailzer


class DescriptionViewset(viewsets.ModelViewSet):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionSerializer

    

class phone_and_tabletProductaddViewset(viewsets.ModelViewSet):
    queryset = phone_and_tabletProductadd.objects.all()
    serializer_class = phone_and_tabletProductaddSerilizer
    pagination_class = All_pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['phoneAndtablet__name',"ipadAndTAB__name","productBrand__name","name"]


    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return phone_and_tabletProductadd.objects.filter(id=params_id)
            except phone_and_tabletProductadd.DoesNotExist:
                return Http404("phone And tablet does not exist for the given params_id")
        return phone_and_tabletProductadd.objects.all()