from django.db import models
from smart_elecotorines.models import productBrand

class SoundAndEquipment(models.Model):
    """ sound and Equipment  models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)



class speaker (models.Model):
    """ spearkers models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)



STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)

class soundSpecificaionModel(models.Model):
    """ Specification Model here now """
    brand = models.ForeignKey(productBrand,on_delete=models.CASCADE,blank=True,null=True)
    ChargingInterface = models.CharField(max_length=350)
    Bluetooth  = models.CharField(max_length=350)
    StorageCapacity = models.CharField(max_length=350)
    StorageType = models.CharField(max_length=350)
    GraphicsModel = models.CharField(max_length=350)
    Model = models.CharField(max_length=350)
    Batterycapacity = models.CharField(max_length=350)
    ANCStatus = models.CharField(max_length=350)
    MicStatus = models.CharField(max_length=350)
    DriverSize = models.CharField(max_length=350,blank=True,null=True)
    SweatWaterResistance = models.CharField(max_length=350,blank=True,null=True)
    WirelessCharging = models.CharField(max_length=350)
    Playtime = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.model


class soundDescriptionModel(models.Model):
    image = models.ImageField(upload_to="phone_and_tablet/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    

    
class soundSpeckerProductAdd (models.Model):
    """  sound spacker ProductAdd """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="sound_equipment/media/image")
    SoundAndEquipment = models.ForeignKey(SoundAndEquipment,on_delete=models.CASCADE,null=True,blank = True)
    speaker = models.ForeignKey(speaker,on_delete=models.CASCADE,null =True,blank=True)
    productBrand = models.ForeignKey(productBrand,on_delete=models.CASCADE,null=True,blank=True)
    soundSpecificaionModel = models.ForeignKey(soundSpecificaionModel,on_delete=models.CASCADE,null=True,blank=True)
    soundDescriptionModel = models.ForeignKey(soundDescriptionModel,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    class Meta:
        ordering = ["price"]


