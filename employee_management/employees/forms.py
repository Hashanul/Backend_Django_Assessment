from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Employee, Department, Achievement

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class EmployeeForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    achievements = forms.ModelMultipleChoiceField(
        queryset=Achievement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'address', 'department', 'achievements']