from django.urls import path
from .views import UserView, AdministratorView, VehicleView, TripView, SalaryView, EmployeeView, SalaryReportView
from django.shortcuts import render

def welcome_view(request):
    return render(request, 'welcome.html')

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('user', UserView.as_view()),
    path('admin', AdministratorView.as_view()),
    path('vehicle', VehicleView.as_view()),
    path('trip', TripView.as_view()),
    path('salary', SalaryView.as_view()),
    path('employee', EmployeeView.as_view()),
    path('salaryreport', SalaryReportView.as_view()),
]