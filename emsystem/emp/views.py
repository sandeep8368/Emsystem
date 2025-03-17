from django.shortcuts import render
from rest_framework import generics
from emp.models import Employee
from emp.serializers import EmployeeSerializers

# Create your views here.
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
    
class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers