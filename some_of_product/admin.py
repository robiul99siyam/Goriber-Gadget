from django.contrib import admin
from .models import BennerSection,feature_product,featured_category,ReadyOfOrder


admin.site.register(BennerSection)
admin.site.register(featured_category)
admin.site.register(feature_product)
admin.site.register(ReadyOfOrder)