from django.urls import path
from .views import (
    welcome_view,
    login_page,
    authenticate_user,
    UserView,
    AdministratorView,
    VehicleView,
    TripView,
    SalaryView,
    EmployeeView,
    SalaryReportView,
)

urlpatterns = [
    # Template views
    path('', welcome_view, name='welcome'),
    path('login/', login_page, name='login'),
    path('authenticate/', authenticate_user, name='authenticate'),
    
    # API views
    path('user/', UserView.as_view(), name='user_api'),
    path('admin/', AdministratorView.as_view(), name='administrator_api'),
    path('vehicle/', VehicleView.as_view(), name='vehicle_api'),
    path('trip/', TripView.as_view(), name='trip_api'),
    path('salary/', SalaryView.as_view(), name='salary_api'),
    path('employee/', EmployeeView.as_view(), name='employee_api'),
    path('salaryreport/', SalaryReportView.as_view(), name='salaryreport_api'),
]
