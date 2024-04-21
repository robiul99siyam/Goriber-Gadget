from django.shortcuts import render
from rest_framework import viewsets
from .models import CoverAndglass,CoverAndGlassProduct,productBrandModel
from .serializer import converGlassSerializer,CoverAndGlassProductSerializer,productBrandSerializer
from rest_framework import filters,pagination
from rest_framework import serializers
from django.http import Http404





class coverGlassViewset(viewsets.ModelViewSet):
    """ Cover Glass Views """
    queryset = CoverAndglass.objects.all()
    serializer_class = converGlassSerializer



class ProductViewset(viewsets.ModelViewSet):
    """ product Views """
    queryset = productBrandModel.objects.all()
    serializer_class = productBrandSerializer


class All_pagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = page_size
    max_page_size = 100



class CoverAndGlassProductAdd(viewsets.ModelViewSet):
    """ product add Views """
    queryset = CoverAndGlassProduct.objects.all()

    serializer_class = CoverAndGlassProductSerializer
    pagination_class = All_pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['coverAndglass__name', 'productBrand__name','name']

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")

        if params_id is not None:
            try:
                return CoverAndGlassProduct.objects.filter(id=params_id)
            except CoverAndGlassProduct.DoesNotExist:
                raise Http404("CoverAndGlassProduct does not exist for the given params_id")
        return CoverAndGlassProduct.objects.all()