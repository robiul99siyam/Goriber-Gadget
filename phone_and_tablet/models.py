from django.db import models


class phoneAndtablet(models.Model):
    """ phone and tablet models """

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self) :
        return self.name

class ipadAndTAB (models.Model):
    """ ipad models """

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

class SpecificationModel (models.Model):

    """ Specification Model here now """
    brand = models.ForeignKey(productBrand,on_delete=models.CASCADE,blank=True,null=True)
    model = models.CharField(max_length=350)
    network = models.CharField(max_length=350)
    Dimensions = models.CharField(max_length=350)
    Weight = models.CharField(max_length=350)
    Sim = models.CharField(max_length=350)
    DisplayType  = models.CharField(max_length=350)
    DisplaySize = models.CharField(max_length=350)
    DisplayResolution = models.CharField(max_length=350)
    os = models.CharField(max_length=350)
    chipset = models.CharField(max_length=350,blank=True,null=True)
    CPU = models.CharField(max_length=350,blank=True,null=True)
    Memory = models.CharField(max_length=350)
    MainCemera = models.CharField(max_length=350)
    SelfieCemera = models.CharField(max_length=350)
    Sound = models.CharField(max_length=350)
    BetteryInfo = models.CharField(max_length=350)
    Sensors = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.model


class DescriptionModel(models.Model):
    image = models.ImageField(upload_to="phone_and_tablet/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description

class phone_and_tabletProductadd (models.Model):
    """  phone_and_tabletProductadd """

    name = models.CharField(max_length=200, null =True, blank = True)
    price = models.CharField(max_length=20,null=True,blank=True)
    product_code = models.CharField(max_length=200,null=True,blank = True)
    image = models.ImageField(upload_to="phone_and_tablet/media/image")
    phoneAndtablet = models.ForeignKey(phoneAndtablet,on_delete=models.CASCADE,null=True,blank = True,related_name="phoneAndtablet")
    ipadAndTAB = models.ForeignKey(ipadAndTAB,on_delete=models.CASCADE,null =True,blank=True,related_name="ipadAndTAB")
    productBrand = models.ForeignKey(productBrand,on_delete=models.CASCADE,null=True,blank=True,related_name="ipadAndTAB")
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    SpecificationModel = models.ForeignKey(SpecificationModel,on_delete=models.CASCADE,null=True,blank=True,related_name="SpecificationModel")
    DescriptionModel = models.ForeignKey(DescriptionModel,on_delete=models.CASCADE,blank=True,null=True,related_name='DescriptionModel')
    class Meta:
        ordering = ["price"]

    def __str__(self) -> str:
        return self.name

