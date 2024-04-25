from .models import powerAndaccessories,PowerProductBrand,cableAndinternconnectProductAdd,PowerAndaccessoriesSpecificaionModel,powerAndaccessoriesDescriptionModel,cableAndinternconnect
from rest_framework import serializers


class PowerAndaccessoriesSpecificaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerAndaccessoriesSpecificaionModel
        fields = '__all__'


        
class CableAndInternet(serializers.ModelSerializer):
    class Meta:
        model = cableAndinternconnect
        fields = '__all_'


class powerAndaccessoriesDescriptionSerailzer(serializers.ModelSerializer):
    class Meta:
        model = powerAndaccessoriesDescriptionModel
        fields = '__all__'




class powerAndaccessrorieSerailzer(serializers.ModelSerializer):
    class Meta:
        model  = powerAndaccessories
        fields = '__all__'
        

class productBrandSerailzer(serializers.ModelSerializer):
    class Meta:
        model  = PowerProductBrand
        fields = '__all__'

class cableAndinternconnectProductAddSerailzer(serializers.ModelSerializer):
    class Meta:
        model  = cableAndinternconnectProductAdd
        fields = '__all__'
