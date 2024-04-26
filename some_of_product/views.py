from django.shortcuts import render
from .models import BennerSection,feature_product,featured_category,ReadyOfOrder
from .serializer import BennerSerializer,feature_prodcutSerializer,feature_categroySerailzer,ReadyofOrderseriailzer
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
            except feature_product.DoesNotExist:
                return Http404("phone And tablet does not exist for the given params_id")
        return feature_product.objects.all()






class featureProductViewset(viewsets.ModelViewSet):
    queryset = feature_product.objects.all()
    serializer_class = feature_prodcutSerializer

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return feature_product.objects.filter(id=params_id)
            except feature_product.DoesNotExist:
                return Http404("phone And tablet does not exist for the given params_id")
        return feature_product.objects.all()
    
    def list (self,request):
        queryset  = feature_product.objects.all()
        serializer = feature_prodcutSerializer(queryset,many=True)

        for product in serializer.data:
            discount_price = product["price"] - product['discount']
            discount_price = product["price"] * 0.8 
            product['discount_price'] = discount_price
            return Response(serializer.data)



class ReadyofOrderViewset(viewsets.ModelViewSet):
    queryset = ReadyOfOrder.objects.all()
    serializer_class = ReadyofOrderseriailzer

    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return ReadyOfOrder.objects.filter(id=params_id)
            except ReadyOfOrder.DoesNotExist:
                return Http404("phone And tablet does not exist for the given params_id")
        return ReadyOfOrder.objects.all()
    
    def list (self,request):
        queryset  = ReadyOfOrder.objects.all()
        serializer = ReadyofOrderseriailzer(queryset,many=True)

        for product in serializer.data:
            discount_price = product["price"] - product['discount']
            discount_price = product["price"] * 0.8 
            product['discount_price'] = discount_price
            return Response(serializer.data)

    
