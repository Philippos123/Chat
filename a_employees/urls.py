from django.urls import path
from .views import employee_login, employee_dashboard

urlpatterns = [
    path('login/', employee_login, name='employee_login'),
    path('dashboard/', employee_dashboard, name='employee_dashboard'),  # Add this line
]