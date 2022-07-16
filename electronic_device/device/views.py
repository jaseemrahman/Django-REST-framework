from django.shortcuts import render
from .models import ElectronicDeviceDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ElectronicDeviceDetailserializers
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def device_list(request):
    if request.method=='GET':
        val=ElectronicDeviceDetail.objects.all()
        serializer=ElectronicDeviceDetailserializers(val, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=ElectronicDeviceDetailserializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST_)


@api_view(['GET','PUT','DELETE']) 
def device_detail(request,id): 
    if request.method=='GET':
        val=ElectronicDeviceDetail.objects.get(pk=id)
        serializer=ElectronicDeviceDetailserializers(val)
        return Response(serializer.data)

    elif request.method=='PUT':
        val=ElectronicDeviceDetail.objects.get(pk=id)
        serializer=ElectronicDeviceDetailserializers(val,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST_)    

    
    elif request.method=='DELETE':
        val=ElectronicDeviceDetail.objects.get(pk=id)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

# @api_view(['POST'])
# def deviceadded(request,id):
#     if request.method=='POST':
#         val=ElectronicDeviceDetail.objects.get(pk=id)
#         serializer=ElectronicDeviceDetailserializers(val,data=request.data)
#         if id is in se:

