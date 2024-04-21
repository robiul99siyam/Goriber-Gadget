from .models import peripheriesProduct,Perpheries
from rest_framework import serializers

class PeriperiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perpheries
        fields = "__all__"



class peripheriesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = peripheriesProduct
        fields = "__all__"