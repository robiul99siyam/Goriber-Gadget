from django.contrib import admin
from .models import powerAndaccessories,cableAndinternconnect,PowerProductBrand,cableAndinternconnectProductAdd,powerAndaccessoriesDescriptionModel,PowerAndaccessoriesSpecificaionModel

model_register = [powerAndaccessories,cableAndinternconnect,PowerProductBrand]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':("name",)}
    list_display = ['name','slug']

for model in model_register:
    admin.site.register(model,AdminModel)


admin.site.register(cableAndinternconnectProductAdd)
admin.site.register(powerAndaccessoriesDescriptionModel)
admin.site.register(PowerAndaccessoriesSpecificaionModel)
