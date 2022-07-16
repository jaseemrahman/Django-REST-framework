# from distutils.command.upload import upload
# from email.mime import image
# from email.policy import default
from django.db import models

# Create your models here.
class ElectronicDeviceDetail(models.Model):
    type=models.CharField(max_length=100)
    brand_name=models.CharField(max_length=100)
    model_number=models.CharField(max_length=25,default=0)
    image=models.ImageField(upload_to='uploads',default='default.jpg')
    serial_number=models.CharField(max_length=25)
    color=models.CharField(max_length=25)
    description=models.TextField(max_length=250)
    price=models.FloatField()
    has_warranty=models.BooleanField()

    def __str__(self):
        return f"Type:{self.type} Brand: {self.brand_name} Model no:{self.model_number}"

    class Meta:
        indexes=[models.Index(fields=['type','brand_name','serial_number'])]
