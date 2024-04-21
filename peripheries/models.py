from django.db import models
from conver_and_glass.models import productBrandModel

class Perpheries(models.Model):
    """ Perpheries models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self) -> str:
        return self.name




STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)
class peripheriesProduct (models.Model):
    """  peripheries model  """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="peripheries/media/image")
    productBrandModel = models.ForeignKey(productBrandModel,on_delete=models.CASCADE,null=True,blank=True)
    Perpheries   = models.ForeignKey(Perpheries,on_delete = models.CASCADE,null = True, blank= True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    
    class Meta:
        ordering = ["price"]



