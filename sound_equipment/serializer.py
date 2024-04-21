from .models import speaker,soundSpeckerProductAdd,SoundAndEquipment,soundDescriptionModel,soundSpecificaionModel
from rest_framework import serializers


class SoundSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = soundSpecificaionModel
        fields = '__all__'


class SoundDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = soundSpecificaionModel
        fields = '__all__'

        

class speakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = speaker
        fields = '__all__'




class soundAndEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundAndEquipment
        fields = '__all__'



class soundSpeckerProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = soundSpeckerProductAdd
        fields = '__all__'


