from django.shortcuts import render
from rest_framework import viewsets
from .models import GamingAndLoptob,BusineesClassLoptob,ultraBook,ProductBrand,laptob_and_destop_productAdd,LaptobDescriptionModel,LaptobSpecificaionModel
from .serializer import GamingAndlaptopSerializer,BusineesClassLoptobSerializer,ultraBookSerializer,ProductBrandSerializer,laptob_and_destop_productAddSerializer,LabtobSpecificationSerializer,LaptobDescriptionSerailzer
from rest_framework import filters
from conver_and_glass.views import All_pagination
from django.http import Http404


class LaptobSpecifationViewset(viewsets.ModelViewSet):
    queryset  = LaptobSpecificaionModel.objects.all()
    serializer_class = LabtobSpecificationSerializer

class LaptobDescriptionViewset(viewsets.ModelViewSet):
    queryset  = LaptobDescriptionModel.objects.all()
    serializer_class = LaptobDescriptionSerailzer


class GamingLaptobViewsets(viewsets.ModelViewSet):
    queryset = GamingAndLoptob.objects.all()
    serializer_class = GamingAndlaptopSerializer


class BusineesClassLoptobViewsets(viewsets.ModelViewSet):
    queryset = BusineesClassLoptob.objects.all()
    serializer_class = BusineesClassLoptobSerializer


class ultraBookViewsets(viewsets.ModelViewSet):
    queryset = ultraBook.objects.all()
    serializer_class = ultraBookSerializer


class ProductBrandViewsets(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer


class laptob_and_destop_productAddViewsets(viewsets.ModelViewSet):
    queryset = laptob_and_destop_productAdd.objects.all()
    serializer_class = laptob_and_destop_productAddSerializer
    pagination_class = All_pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['productBrand__name', 'BusineesClassLoptob__name,ultraBook__name',"Macbook__name","GamingAndLoptob__name"]

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return laptob_and_destop_productAdd.objects.filter(id=params_id)
            except laptob_and_destop_productAdd.DoesNotExist:
                return Http404("Laptob and desktop does not exist for the given params_id")
        return laptob_and_destop_productAdd.objects.all()


