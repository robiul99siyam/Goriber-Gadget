from django.db import models
from conver_and_glass.models import productBrandModel

class fitnessAndwearable(models.Model):
    """ fitness ans wearable models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fitness and Wearable"
        verbose_name_plural = "Fitness and Wearables"
   


class watachAndaccessories(models.Model):
    """ watch and accessories models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Watch And Accessories"
        verbose_name_plural = "Watch And Accessories"


    


class FitnessSpecificaionModel(models.Model):
    """ Specification Model here now """
    brand = models.ForeignKey(productBrandModel,on_delete=models.CASCADE,blank=True,null=True)
    Model = models.CharField(max_length=350)
    DisplaySize = models.CharField(max_length=350)
    Compatiblewith  = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)
    
    def __str__(self) -> str:
        return self.model
    class Meta:
        verbose_name = "Fitness Specification Model"
        verbose_name_plural = "Fitness Specifications"



class FitnessDescriptionModel(models.Model):
    image = models.ImageField(upload_to="phone_and_tablet/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "Fitness Description Model"
        verbose_name_plural = "Fitness Descriptions"




    
STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)




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
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    class Meta:
        ordering = ["price"]
        verbose_name = "Fitness_and_wearable_Product"
        verbose_name_plural = "Fitness and wearable Products "
    