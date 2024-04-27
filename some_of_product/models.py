from django.db import models

# Create your models here.

class BennerSection(models.Model):
    image = models.ImageField(upload_to="some_of_product/media/image/")

class featured_category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="some_of_product/media/image/")

    def __str__(self):
        return self.name 


class FeatureProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to="some_of_product/media/image",blank=True,null=True)


class ReadyOfOrder(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to="some_of_product/media/image",blank=True,null=True)


