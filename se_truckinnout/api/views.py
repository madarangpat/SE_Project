from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import UserSerializer, AdministratorSerializer, VehicleSerializer, TripSerializer, SalarySerializer, EmployeeSerializer, SalaryReportSerializer
from .models import User, Administrator, Vehicle, Trip, Salary, Employee, SalaryReport
from django.contrib.auth import authenticate, login

# Create your views here.

def welcome_view(request):
    return render(request, 'welcome.html')

def login_page(request):
    return render(request, 'login.html')

from django.shortcuts import redirect

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            return redirect('/')  # Redirect to the home page or dashboard
        else:
            # If authentication fails, redirect back to the login page with an error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return redirect('login')  # Redirect back to login on GET

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
    