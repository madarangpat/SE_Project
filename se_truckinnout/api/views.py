from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, AdministratorSerializer, VehicleSerializer, TripSerializer, SalarySerializer, EmployeeSerializer, SalaryReportSerializer
from .models import User, Administrator, Vehicle, Trip, Salary, Employee, SalaryReport

# Create your views here.

def welcome_view(request):
    return render(request, 'welcome.html')
#======================Welcome Page===================

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class AdministratorView(generics.CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    
class VehicleView(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
class TripView(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
class SalaryView(generics.CreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    
class EmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class SalaryReportView(generics.CreateAPIView):
    queryset = SalaryReport.objects.all()
    serializer_class = SalaryReportSerializer
    
#======================CreateAPIView======================
    