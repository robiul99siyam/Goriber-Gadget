from .models import GamingAndLoptob,BusineesClassLoptob,ultraBook,ProductBrand,laptob_and_destop_productAdd,LaptobDescriptionModel,LaptobSpecificaionModel,Macbook
from rest_framework import serializers


class MackBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macbook
        fields = '__all__'

class LaptobDescriptionSerailzer(serializers.ModelSerializer):
    class Meta:
        model = LaptobDescriptionModel
        fields = '__all__'

class LabtobSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptobSpecificaionModel
        fields = '__all__'        
class GamingAndlaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamingAndLoptob
        fields = '__all__'

class BusineesClassLoptobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusineesClassLoptob
        fields = '__all__'

class ultraBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ultraBook
        fields = '__all__'

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'

class laptob_and_destop_productAddSerializer(serializers.ModelSerializer):
    LaptobDescriptionModel = LaptobDescriptionSerailzer()
    class Meta:
        model = laptob_and_destop_productAdd
        fields = '__all__'
    
