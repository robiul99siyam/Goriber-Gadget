from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cover_and_glass/',include("conver_and_glass.urls")),
    path('fitness_and_wearable/',include("fitness_and_wearable.urls")),
    path('loptob_and_desktop/',include("loptob_and_desktop.urls")),
    path('peripheries/',include("peripheries.urls")),
    path('phone_and_tablet/',include("phone_and_tablet.urls")),
    path('power_and_accessories/',include("power_and_accessories.urls")),
    path('smart_elecotorines/',include("smart_elecotorines.urls")),
    path('sound_equipment/',include("sound_equipment.urls")),
    path('uesr_Devices/',include("uesr_Devices.urls")),
    path('all_product/',include("all_product.urls")),
    path('some_of_product/',include("some_of_product.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)