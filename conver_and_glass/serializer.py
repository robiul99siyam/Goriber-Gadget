from .models import CoverAndglass,productBrandModel,CoverAndGlassProduct
from rest_framework import serializers

class converGlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverAndglass
        fields = '__all__'


class productBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = productBrandModel
        fields = '__all__'


class CoverAndGlassProductSerializer(serializers.ModelSerializer):
    productBrand = productBrandSerializer()
    coverAndglass = converGlassSerializer()  
    class Meta:
        model = CoverAndGlassProduct
        fields = '__all__'
    