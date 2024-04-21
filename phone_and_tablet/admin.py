from django.contrib import admin
from .models import ipadAndTAB,phoneAndtablet,productBrand,phone_and_tabletProductadd,SpecificationModel,DescriptionModel

model_register = [ipadAndTAB,phoneAndtablet,productBrand]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':("name",)}
    list_display = ['name','slug']

for model in model_register:
    admin.site.register(model,AdminModel)
admin.site.register(phone_and_tabletProductadd)
admin.site.register(SpecificationModel)
admin.site.register(DescriptionModel)


