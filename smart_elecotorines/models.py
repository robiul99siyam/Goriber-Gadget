from django.db import models


class smartAndelectines(models.Model):
    """ smart and elecotines models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)
    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = "smartAndelectines"
        verbose_name_plural = "Smart And electines"

    


class mediaAndStreams (models.Model):
    """ media and streams models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self) :
        return self.name
    


class productBrand(models.Model):

    """ prodcut brand model """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self) :
        return self.name
    



STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)

class SmartSpecificaionModel(models.Model):
    """ Specification Model here now """
    brand = models.ForeignKey(productBrand,on_delete=models.CASCADE,blank=True,null=True)
    PowerOutput = models.CharField(max_length=350)
    Model = models.CharField(max_length=350)
    Batterycapacity = models.CharField(max_length=350)
    Inputinterface  = models.CharField(max_length=350)
    color = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.model
    class Meta:
        verbose_name = "Smart Specificaion Model"
        verbose_name_plural = "Smart Specificaions"


class SmartDescriptionModel(models.Model):
    image = models.ImageField(upload_to="smart_elecotorines/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Smart Description Model"
        verbose_name_plural = "Smart Descriptions "

    

class smart_elecotorinesProductAdd (models.Model):
    """  smart_elecotorinesProductAdd """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="smart_elecotorines/media/image")
    smartAndelectines = models.ForeignKey(smartAndelectines,on_delete=models.CASCADE,null=True,blank = True)
    mediaAndStreams = models.ForeignKey(mediaAndStreams,on_delete=models.CASCADE,null =True,blank=True)
    productBrand = models.ForeignKey(productBrand,on_delete=models.CASCADE,null=True,blank=True)
    SmartSpecificaionModel = models.ForeignKey(SmartSpecificaionModel,on_delete=models.CASCADE,null=True,blank=True)
    SmartDescriptionModel = models.ForeignKey(SmartDescriptionModel,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    class Meta:
        ordering = ["price"]

    