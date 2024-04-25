from .models import BennerSection
from rest_framework import serializers

class BennerSctionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = BennerSection
        fields = '__all__'