from django.contrib import admin
from .models import Perpheries,peripheriesProduct

class PerpheriesAdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Perpheries,PerpheriesAdminModel)
admin.site.register(peripheriesProduct)