from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        # Ensure the user is an employee
        if user is not None and user.is_staff:  # Assuming staff users are employees
            login(request, user)
            return redirect('employee_dashboard')  # Change to your desired URL
        else:
            messages.error(request, 'Invalid credentials or unauthorized access.')
    
    return render(request, 'a_employees/employee_login.html') 

@login_required
def employee_dashboard(request):
    return render(request, 'a_employees/employee_dashboard.html')  # Create this template