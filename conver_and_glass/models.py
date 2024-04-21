from django.db import models

class CoverAndglass(models.Model):
    """ cover and glass models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name

class productBrandModel(models.Model):
    """ brand  models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name



STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)
class CoverAndGlassProduct(models.Model):
    """ cover and glass product """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="conver_and_glass/media/image")
    coverAndglass = models.ForeignKey(CoverAndglass,on_delete=models.CASCADE,null=True,blank = True)
    productBrand = models.ForeignKey(productBrandModel,on_delete=models.CASCADE,null=True,blank = True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
 
    class Meta:
        ordering = ["price"]