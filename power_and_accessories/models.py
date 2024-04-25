from django.db import models


class powerAndaccessories(models.Model):
    """  power and accessories models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)


    def __str__(self) :
        return self.name


    class Meta:
        verbose_name = "power And accessories"
        verbose_name_plural = "power And Accessories"



class cableAndinternconnect  (models.Model):
    """ cable and internconnect models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)


    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = "cable And internconnect"
        verbose_name_plural = " cable And Internconnect"
    




class PowerProductBrand(models.Model):

    """ prodcut brand model """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self) :
        return self.name




STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)




class PowerAndaccessoriesSpecificaionModel(models.Model):
    """ Specification Model here now """
    brand = models.ForeignKey(PowerProductBrand,on_delete=models.CASCADE,blank=True,null=True)
    PowerOutput = models.CharField(max_length=350)
    Model = models.CharField(max_length=350)
    Batterycapacity = models.CharField(max_length=350)
    Inputinterface  = models.CharField(max_length=350)
    color = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.model
    class Meta:
        verbose_name = "PowerAndaccessoriesSpecificaionModel"
        verbose_name_plural = "Power And Accessories Specificaions"



class powerAndaccessoriesDescriptionModel(models.Model):
    image = models.ImageField(upload_to="power_and_accessories/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "powerAndaccessoriesDescriptionModel"
        verbose_name_plural = "Power And Accessories Descriptions"


    


class cableAndinternconnectProductAdd (models.Model):
    """  laptob_and_destop """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="power_and_accessories/media/image")
    powerAndaccessories = models.ForeignKey(powerAndaccessories,on_delete=models.CASCADE,null=True,blank = True)
    cableAndinternconnect = models.ForeignKey(cableAndinternconnect,on_delete=models.CASCADE,null =True,blank=True)
    PowerProductBrand = models.ForeignKey(PowerProductBrand,on_delete=models.CASCADE,null=True,blank=True)
    PowerAndaccessoriesSpecificaionModel = models.ForeignKey(PowerAndaccessoriesSpecificaionModel,on_delete=models.CASCADE,null=True,blank=True)
    powerAndaccessoriesDescriptionModel = models.ForeignKey(powerAndaccessoriesDescriptionModel,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    class Meta:
        ordering = ["price"]
        verbose_name = "cable And internconnect ProductAdd"
        verbose_name_plural = "Cable And Internconnect ProductAdds"
