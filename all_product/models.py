from django.db import models

# Create your models here.

class BennerSection(models.Model):
    image = models.ImageField("all_product/up_load/")
