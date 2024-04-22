from django.contrib import admin
from .models import smartAndelectines,mediaAndStreams,productBrand,smart_elecotorinesProductAdd,SmartDescriptionModel,SmartSpecificaionModel

model_register = [smartAndelectines,mediaAndStreams,productBrand]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':("name",)}
    list_display = ['name','slug']

for model in model_register:
    admin.site.register(model,AdminModel)


admin.site.register(smart_elecotorinesProductAdd)
admin.site.register(SmartDescriptionModel)
admin.site.register(SmartSpecificaionModel)