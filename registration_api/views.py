from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.
# Read
@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        Customer_obj=Customer.objects.all() #queryset
        serializer=CustomerSerializer(Customer_obj, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
            

         
            
           

         
   

       

""" #create
@api_view(['POST'])
def post_Customer(request):
    Customer_obj=Customer.objects.all() #queryset
    serializer=CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) """


#update
@api_view(['PUT'])
def update_Customer(request,id):
    Customer_obj=Customer.objects.get(id=id) #queryset
    serializer=CustomerSerializer(instance=Customer_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, id):
    if request.method == "DELETE":
        cust = Customer.objects.get(id=id)
        update_Customer={}
        for field in cust._meta.fields:
         update_Customer[field.name] = 'X'
        cust.__class__.objects.filter(id=id).update(**update_Customer)
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

