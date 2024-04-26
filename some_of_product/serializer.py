from .models import BennerSection,featured_category,feature_product,ReadyOfOrder
from rest_framework import serializers


class BennerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BennerSection
        fields = '__all__'

class feature_categroySerailzer(serializers.ModelSerializer):
    class Meta:
        model = featured_category
        fields = '__all__'


class feature_prodcutSerializer(serializers.ModelSerializer):

    class Meta:
        model = feature_product
        fields = "__all__"


class ReadyofOrderseriailzer(serializers.ModelSerializer):
    class Meta:
        model = ReadyOfOrder
        fields = '__all__'