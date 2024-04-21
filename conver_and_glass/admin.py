from django.contrib import admin
from .models import CoverAndglass,CoverAndGlassProduct,productBrandModel

model_register = [CoverAndglass,productBrandModel]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name",'slug']

for model in model_register:
    admin.site.register(model,AdminModel)

class product_cover_and_glass(admin.ModelAdmin):
    list_display = ['name','price','product_code']
admin.site.register(CoverAndGlassProduct,product_cover_and_glass)
