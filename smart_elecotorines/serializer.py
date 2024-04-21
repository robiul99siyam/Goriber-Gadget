from .models import productBrand,smart_elecotorinesProductAdd,mediaAndStreams,smartAndelectines,SmartDescriptionModel,SmartSpecificaionModel
from rest_framework import serializers


class SmartDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartDescriptionModel
        fields = "__all__"


class SmartSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SmartSpecificaionModel
        fields  = "__all__"
        


class ProductBrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = productBrand
        fields = '__all__'


class smart_elecotorinesProductAddSerilizer(serializers.ModelSerializer):
    class Meta:
        model = smart_elecotorinesProductAdd
        fields = '__all__'


class mediaAndStreamsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = mediaAndStreams
        fields = '__all__'


class smartAndelectinesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = smartAndelectines
        fields = '__all__'