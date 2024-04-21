from django.db import models
from conver_and_glass.models import productBrandModel

class fitnessAndwearable(models.Model):
    """ fitness ans wearable models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name

class watachAndaccessories(models.Model):
    """ watch and accessories models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name

    
STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)


class FitnessSpecificaionModel(models.Model):
    """ Specification Model here now """
    brand = models.ForeignKey(productBrandModel,on_delete=models.CASCADE,blank=True,null=True)
    Model = models.CharField(max_length=350)
    DisplaySize = models.CharField(max_length=350)
    Compatiblewith  = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)
    
    def __str__(self) -> str:
        return self.model





class FitnessDescriptionModel(models.Model):
    image = models.ImageField(upload_to="phone_and_tablet/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    

class Fitness_and_wearable_Product(models.Model):
    """ cover and glass product """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="fitness_and_wearable/media/image")
    watachAndaccessories = models.ForeignKey(watachAndaccessories,on_delete=models.CASCADE,null=True,blank = True)
    fitnessAndwearable = models.ForeignKey(fitnessAndwearable,on_delete=models.CASCADE,null =True,blank=True)
    productBrandModel = models.ForeignKey(productBrandModel,on_delete=models.CASCADE,null=True,blank=True)
    FitnessSpecificaionModel = models.ForeignKey(FitnessSpecificaionModel,on_delete=models.CASCADE,null=True,blank=True)
    FitnessDescriptionModel = models.ForeignKey(FitnessDescriptionModel,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    class Meta:
        ordering = ["price"]
