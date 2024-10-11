from django.contrib import admin
# No need to import User or register it again
# from django.contrib.auth.models import User

# If you have other models in your `a_employees` app, register them here.
# For example, if you have an Employee model (if you decide to create one):
# from .models import Employee
# admin.site.register(Employee)

# If you want to customize the User model in the admin, do it like this:
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # Add any customizations for the User admin here
    pass  # You can add additional fields or customization

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, CustomUserAdmin)  # Register your custom admin