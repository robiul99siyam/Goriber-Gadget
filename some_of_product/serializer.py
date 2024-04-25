from .models import BennerSection
from rest_framework import serializers


class BennerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BennerSection
        fields = '__all__'
        