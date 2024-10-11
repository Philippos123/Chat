from django import forms
from .models import EmployeeProfile

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['position', 'other_fields']  # Specify fields you want to include