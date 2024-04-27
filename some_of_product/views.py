from django.shortcuts import render
from .models import BennerSection,featured_category,FeatureProduct,ReadyOfOrder
from .serializer import BennerSerializer,feature_categroySerailzer,FeatureProductSerializer,ReadyOfOrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import Http404


class BennerViewset(viewsets.ModelViewSet):
    queryset = BennerSection.objects.all()
    serializer_class = BennerSerializer



class FeaturedCategoryViewset(viewsets.ModelViewSet):
    queryset = featured_category.objects.all()
    serializer_class = feature_categroySerailzer


    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return featured_category.objects.filter(id=params_id)
            except featured_category.DoesNotExist:
                return Http404("Featured Category Viewset does not exist for the given params_id")
        return featured_category.objects.all()





class featureProductViewset(viewsets.ModelViewSet):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return FeatureProduct.objects.filter(id=params_id)
            except FeatureProduct.DoesNotExist:
                raise Http404("featureProductViewsetdoes not exist for the given params_id")
        return FeatureProduct.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for product in serializer.data:
         
            discount_price = product["price"] * (1 - product['discount'] / 100)  
         
            product['discounted_price'] = discount_price
        return Response(serializer.data)







class ReadyofOrderViewset(viewsets.ModelViewSet):
    queryset = ReadyOfOrder.objects.all()
    serializer_class = ReadyOfOrderSerializer

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return ReadyOfOrder.objects.filter(id=params_id)
            except ReadyOfOrder.DoesNotExist:
                return Http404("phone And tablet does not exist for the given params_id")
        return ReadyOfOrder.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for product in serializer.data:
         
            discount_price = product["price"] * (1 - product['discount'] / 100)  
         
            product['discounted_price'] = discount_price
        return Response(serializer.data)
