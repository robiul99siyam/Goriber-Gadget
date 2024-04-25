from rest_framework import filters,generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.http import Http404

''""" all model add """
from conver_and_glass.models import CoverAndGlassProduct
from fitness_and_wearable.models import Fitness_and_wearable_Product
from loptob_and_desktop.models import laptob_and_destop_productAdd
from peripheries.models import peripheriesProduct
from phone_and_tablet.models import phone_and_tabletProductadd
from power_and_accessories.models import cableAndinternconnectProductAdd
from smart_elecotorines.models import smart_elecotorinesProductAdd
from sound_equipment.models import soundSpeckerProductAdd

''""" all serializer add  """
from conver_and_glass.serializer import CoverAndGlassProductSerializer
from fitness_and_wearable.serializer import Fitness_and_wearable_ProductSerializers
from loptob_and_desktop.serializer import laptob_and_destop_productAddSerializer
from peripheries.serializer import peripheriesProductSerializer
from phone_and_tablet.serializer import phone_and_tabletProductaddSerilizer
from power_and_accessories.serializer import cableAndinternconnectProductAddSerailzer
from smart_elecotorines.serializer import smart_elecotorinesProductAddSerilizer
from sound_equipment.serializer import soundAndEquipmentSerializer

class TextViewApi(ObjectMultipleModelAPIView):
    querylist = [
        {"queryset": CoverAndGlassProduct.objects.all(), "serializer_class": CoverAndGlassProductSerializer},

        {"queryset": Fitness_and_wearable_Product.objects.all(), "serializer_class": Fitness_and_wearable_ProductSerializers},

        {"queryset": laptob_and_destop_productAdd.objects.all(), "serializer_class": laptob_and_destop_productAddSerializer},

        {"queryset": peripheriesProduct.objects.all(), "serializer_class": peripheriesProductSerializer},

        {"queryset": phone_and_tabletProductadd.objects.all(), "serializer_class": phone_and_tabletProductaddSerilizer},

        {"queryset": cableAndinternconnectProductAdd.objects.all(), "serializer_class": cableAndinternconnectProductAddSerailzer},

        {"queryset": smart_elecotorinesProductAdd.objects.all(), "serializer_class": smart_elecotorinesProductAddSerilizer},


        {"queryset": soundSpeckerProductAdd.objects.all(), "serializer_class": soundAndEquipmentSerializer},

    ]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price', 'product_code']  


