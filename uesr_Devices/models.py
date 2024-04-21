from django.db import models

class UserDevice(models.Model):
    device_name = models.CharField(max_length=250)
    bh = models.CharField(max_length=250)
    count = models.CharField(max_length=250)
    price = models.CharField(max_length=12)
    remarks = models.CharField(max_length=12)


    def __str__(self):
        return self.device_name