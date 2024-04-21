from .models import phone_and_tabletProductadd,phoneAndtablet,productBrand,ipadAndTAB,SpecificationModel,DescriptionModel
from rest_framework import serializers

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationModel
        fields = "__all__"
        

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = "__all__"


class PhoneAndtabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = phoneAndtablet
        fields = "__all__"


class ProductBrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = productBrand
        fields = '__all__'



class ipadAndTabSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ipadAndTAB
        fields = '__all__'




class specficationSerailzer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationModel
        fields = '__all__'




class phone_and_tabletProductaddSerilizer(serializers.ModelSerializer):
    phoneAndtablet = PhoneAndtabletSerializer()
    ipadAndTAB = ipadAndTabSerilizer()
    productBrand = ProductBrandSerilizer()
    SpecificationModel = specficationSerailzer()
    class Meta:
        model = phone_and_tabletProductadd
        fields = '__all__'