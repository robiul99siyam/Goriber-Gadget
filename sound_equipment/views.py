from django.shortcuts import render
from .models import soundSpeckerProductAdd,speaker,SoundAndEquipment,soundSpecificaionModel,soundDescriptionModel
from .serializer import soundAndEquipmentSerializer,speakerSerializer,soundSpeckerProductAddSerializer,SoundSpecificationSerializer,SoundDescriptionSerializer


from rest_framework import viewsets
from rest_framework import filters
from conver_and_glass.views import All_pagination
from django.http import Http404

class SoundSpecificationViewsets(viewsets.ModelViewSet):
    queryset = soundSpecificaionModel.objects.all()
    serializer_class =  SoundSpecificationSerializer


class SoundDescriptionViewsets(viewsets.ModelViewSet):
    queryset = soundDescriptionModel.objects.all()
    serializer_class =  SoundDescriptionSerializer


class speckerViewset(viewsets.ModelViewSet):
    queryset = speaker.objects.all()
    serializer_class = speakerSerializer


class SoundAndEquipmentViewset(viewsets.ModelViewSet):
    queryset = SoundAndEquipment.objects.all()
    serializer_class = soundAndEquipmentSerializer


class soundSpeckerProductAddViewset(viewsets.ModelViewSet):
    queryset = soundSpeckerProductAdd.objects.all()
    serializer_class = soundSpeckerProductAddSerializer
    pagination_class = All_pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["SoundAndEquipment__name","speaker__name","productBrand__name"]
    
    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return soundSpeckerProductAdd.objects.filter(id=params_id)
            except soundSpeckerProductAdd.DoesNotExist:
                return Http404("sound and Equipment does not exist for gaven params id ")
        return soundSpeckerProductAdd.objects.all()