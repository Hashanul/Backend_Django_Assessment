from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Employee, Department, Achievement

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with that email already exists.')
        return email
        
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


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