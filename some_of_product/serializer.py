from .models import BennerSection,featured_category,FeatureProduct,ReadyOfOrder
from rest_framework import serializers


class BennerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BennerSection
        fields = '__all__'

class feature_categroySerailzer(serializers.ModelSerializer):
    class Meta:
        model = featured_category
        fields = '__all__'


class FeatureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureProduct
        fields = "__all__"

class ReadyOfOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyOfOrder
        fields = "__all__"



