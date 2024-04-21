from django.contrib import admin
from .models import fitnessAndwearable, watachAndaccessories,Fitness_and_wearable_Product,FitnessDescriptionModel,FitnessSpecificaionModel

model_register = [fitnessAndwearable, watachAndaccessories]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in model_register:
    admin.site.register(model, AdminModel)

admin.site.register(Fitness_and_wearable_Product)
admin.site.register(FitnessSpecificaionModel)
admin.site.register(FitnessDescriptionModel)

