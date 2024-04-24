from django.db import models


class GamingAndLoptob(models.Model):

    """ gaming and loptob models """
    name = models.CharField(max_length=200,null=True,blank =True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class Macbook(models.Model):

    """ macbook models """
    name = models.CharField(max_length=200,null=True,blank =True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class ultraBook(models.Model):

    """ urltra book  models """
    name = models.CharField(max_length=200,null=True,blank =True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.name


    

class BusineesClassLoptob(models.Model):

    """ bussiness class  loptob models """
    name = models.CharField(max_length=200,null=True,blank =True)
    slug = models.SlugField(max_length=200,null=True,blank=True)


    def __str__(self) -> str:
        return self.name


class ProductBrand(models.Model):
    """ product models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.name




STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)


class LaptobSpecificaionModel(models.Model):
    """ Specification Model here now """
    brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,blank=True,null=True)
    Dimension = models.CharField(max_length=350)
    KeyboardType  = models.CharField(max_length=350)
    StorageCapacity = models.CharField(max_length=350)
    StorageType = models.CharField(max_length=350)
    GraphicsModel = models.CharField(max_length=350)
    Model = models.CharField(max_length=350)
    Graphics = models.CharField(max_length=350)
    InterfacePort = models.CharField(max_length=350)
    Weight = models.CharField(max_length=350)
    DisplayType = models.CharField(max_length=350,blank=True,null=True)
    DisplayResulation = models.CharField(max_length=350,blank=True,null=True)
    DisplaySize = models.CharField(max_length=350)
    AdapterType = models.CharField(max_length=350)
    os = models.CharField(max_length=350)
    Chipset = models.CharField(max_length=350)
    Memory = models.CharField(max_length=350)
    Audio = models.CharField(max_length=350)
    BatteryInfo = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.model
    class Meta:
        verbose_name = "Laptob Specificaion Model"
        verbose_name_plural = "Laptob Specificaions"



class LaptobDescriptionModel(models.Model):
    image = models.ImageField(upload_to="loptob_and_desktop/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "Laptob Description Model"
        verbose_name_plural = "Laptop Descriptions"

class laptob_and_destop_productAdd (models.Model):
    """  laptob_and_destop """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="loptob_and_desktop/media/image")
    GamingAndLoptob = models.ForeignKey(GamingAndLoptob,on_delete=models.CASCADE,null=True,blank = True)
    Macbook = models.ForeignKey(Macbook,on_delete=models.CASCADE,null =True,blank=True)
    ultraBook = models.ForeignKey(ultraBook,on_delete=models.CASCADE,null=True,blank=True)
    BusineesClassLoptob = models.ForeignKey(BusineesClassLoptob,on_delete=models.CASCADE,null=True,blank=True)
    ProductBrand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    LaptobSpecificaionModel = models.ForeignKey(LaptobSpecificaionModel,on_delete=models.CASCADE,null=True,blank=True)
    LaptobDescriptionModel = models.ForeignKey(LaptobDescriptionModel,null=True,blank=True,on_delete=models.CASCADE)

    

    class Meta:
        ordering = ["price"]
    
    def __str__(self):
        return self.name



