from django.contrib import admin
from .models import SoundAndEquipment,speaker,soundSpeckerProductAdd,soundDescriptionModel,soundSpecificaionModel

model_register = [SoundAndEquipment,speaker]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':("name",)}
    list_display = ['name','slug']

for model in model_register:
    admin.site.register(model,AdminModel)



admin.site.register(soundSpeckerProductAdd)
admin.site.register(soundSpecificaionModel)
admin.site.register(soundDescriptionModel)