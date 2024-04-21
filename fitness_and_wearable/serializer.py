from .models import fitnessAndwearable,Fitness_and_wearable_Product,watachAndaccessories,FitnessDescriptionModel,FitnessSpecificaionModel
from rest_framework.serializers import ModelSerializer


class fitnessAndwearableSerializers(ModelSerializer):
    class Meta:
        model = fitnessAndwearable
        fields = '__all__'
        


class watachAndaccessoriesSerializers(ModelSerializer):
    class Meta:
        model = watachAndaccessories
        fields = '__all__'


class FitnessDescriptionSerializer(ModelSerializer):
    class  Meta:
        model = FitnessDescriptionModel
        fields = '__all__'

class FitnessSpceificationSerailzer(ModelSerializer):
    class Meta:
        model = FitnessSpecificaionModel
        fields = '__all__'

class Fitness_and_wearable_ProductSerializers(ModelSerializer):
    class Meta:
        model = Fitness_and_wearable_Product
        fields = '__all__'
    