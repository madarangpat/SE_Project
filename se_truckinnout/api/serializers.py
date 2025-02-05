from rest_framework import serializers
from .models import User, Administrator, Vehicle, Trip, Salary, Employee, SalaryReport

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
# Administrator Serializer (Includes User)
class AdministratorSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )   
    class Meta:
        model = Administrator
        fields = '__all__'
        
# Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        
# Trip Serializer (Includes Vehicle)
class TripSerializer(serializers.ModelSerializer):
    vehicle = serializers.SlugRelatedField(
        queryset=Vehicle.objects.all(), slug_field='vehicle_id'
    )    
    class Meta:
        model = Trip
        fields = '__all__'
        
# Salary Serializer 
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
        
# Employee Serializer (Includes User & Trip)
class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    trip = serializers.PrimaryKeyRelatedField(
        queryset = Trip.objects.all()
    )
    class Meta:
        model = Employee
        fields = '__all__'
        
# Salary Report Serializer (Includes Salary & Employee)
class SalaryReportSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(
        queryset = Employee.objects.all()
    )
    salary = serializers.PrimaryKeyRelatedField(
        queryset = Salary.objects.all()
    )
    class Meta:
        model = SalaryReport
        fields = '__all__'