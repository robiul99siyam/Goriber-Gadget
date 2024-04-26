from django.db import models

# Create your models here.

class BennerSection(models.Model):
    image = models.ImageField(upload_to="some_of_product/media/images/")

class featured_category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="some_of_product/media/images/")

    def __str__(self):
        return self.name 


class ReadyOfOrder(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to="some_of_product/media/images/")

    def discount_price (self):
        return self.price - self.discount



class feature_product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to="some_of_product/media/images/")


    def __str__(self):
        return self.name