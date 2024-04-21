from django.contrib import admin
from .models import GamingAndLoptob,ultraBook,BusineesClassLoptob,Macbook,ProductBrand,laptob_and_destop_productAdd,LaptobDescriptionModel,LaptobSpecificaionModel
model_register = [GamingAndLoptob,ultraBook,BusineesClassLoptob,Macbook,ProductBrand]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in model_register:
    admin.site.register(model, AdminModel)

admin.site.register(laptob_and_destop_productAdd)
admin.site.register(LaptobSpecificaionModel)
admin.site.register(LaptobDescriptionModel)