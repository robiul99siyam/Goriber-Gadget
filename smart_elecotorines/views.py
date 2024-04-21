from django.shortcuts import render
from .models import productBrand,smart_elecotorinesProductAdd,mediaAndStreams,smartAndelectines,SmartSpecificaionModel,SmartDescriptionModel
from .serializer import ProductBrandSerilizer,smart_elecotorinesProductAddSerilizer,mediaAndStreamsSerilizer,smartAndelectinesSerilizer,SmartDescriptionSerializer,SmartSpecificationSerializer
from conver_and_glass.views import All_pagination
from rest_framework import viewsets
from rest_framework import filters
from django.http import Http404

class SmartSpecificationViewsets(viewsets.ModelViewSet):
    queryset = SmartSpecificaionModel.objects.all()
    serializer_class = SmartSpecificationSerializer


class SmartDescription(viewsets.ModelViewSet):
    queryset = SmartDescriptionModel.objects.all()
    serializer_class = SmartDescriptionSerializer

class ProductBrandViewsets(viewsets.ModelViewSet):
    queryset = productBrand.objects.all()
    serializer_class = ProductBrandSerilizer


class mediaAndStreamsViewsets(viewsets.ModelViewSet):
    queryset = mediaAndStreams.objects.all()
    serializer_class = mediaAndStreamsSerilizer

class smartAndelectinesViewsets(viewsets.ModelViewSet):
    queryset = smartAndelectines.objects.all()
    serializer_class = smartAndelectinesSerilizer

class smart_elecotorinesProductAddViewsets(viewsets.ModelViewSet):
    queryset = smart_elecotorinesProductAdd.objects.all()
    serializer_class = smart_elecotorinesProductAddSerilizer
    pagination_class = All_pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['smartAndelectines__name','mediaAndStreams__name',"productBrand__name",'name']

    def get_queryset(self):
        params_id = self.request.params_query.get("params_id")

        if params_id is not None:
            try:
                return smart_elecotorinesProductAdd.objects.filter(id=params_id)
            except smart_elecotorinesProductAdd.DoesNotExist:
                return Http404("smart elcotornies  does not exist for the given params_id")
        return smart_elecotorinesProductAdd.objects.all()