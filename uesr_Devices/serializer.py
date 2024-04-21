from .models import UserDevice
from rest_framework import serializers

class UserDeveicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = "__all__"