from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import ElectronicDeviceDetail

class ElectronicDeviceDetailserializers(serializers.ModelSerializer):
    class Meta:
        model=ElectronicDeviceDetail
        fields='__all__'

