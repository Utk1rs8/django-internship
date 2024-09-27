from django.shortcuts import render

# Create your views here.
from .models import Bike
from .serializers import BikesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from rest_framework import status
from rest_framework import generics

class BikeList(APIView):
    def get(self,request):
        bikes = Bike.objects.all()
        serializer = BikesSerializer(bikes,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer =BikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

class BikeDetail(APIView):
    def get(self,request,pk):
        try: 
            bike=Bike.objects.get(pk=pk) 
        except Bike.DoesNotExist: 
            return Response({'msg':'Detail not found'},status=status.HTTP_404_NOT_FOUND) 
        serializer = BikesSerializer(bike) 
        return Response(serializer.data)

    def put(self,request,pk):
        bike=Bike.objects.get(pk=pk)
        serializer = BikesSerializer(bike,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Updated Successfully"})
        else: return Response(serializer.error)

    def delete(self,request,pk):
        bike=Bike.objects.get(pk=pk)
        bike.delete()
        return Response({'msg':"Data Deleted Successfilly"})

# generic class based api
# class BikeList(generics.ListCreateAPIView):
#     bike = Bike.objects.all()
#     serializer = BikesSerializer


# class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
#     bike = Bike.objects.all()
#     serializer = BikesSerializer
def register(request):
        form = AdminRegistrationsForm()
        if request.method == 'POST':
                data = AdminRegistrationsForm(request.POST)
                if data.is_valid():
                    name=data.cleaned_data['name']
                    email=data.cleaned_data['email']
                    contact=data.cleaned_data['mobile']
                    password = data.cleaned_data['password']
                    print(name,email,contact,password)
                    data.save()
                    msg="Registration Successfully"
                    return render(request,'register.html',{'form':form,'msg':msg})
        else:
             return render(request,'register.html',{'form':form})
                

