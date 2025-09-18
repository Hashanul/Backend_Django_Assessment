from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee, Department, Achievement
from .forms import CustomUserCreationForm, EmployeeForm

# Custom logout view to allow GET requests
@csrf_exempt
def user_logout(request):
    if request.method in ["POST", "GET"]:
        logout(request)
        return redirect('login')
    return redirect('employee_list')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employee_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'employees/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_list')
    else:
        form = AuthenticationForm()
    return render(request, 'employees/login.html', {'form': form})

@login_required
def employee_list(request):
    employees = Employee.objects.select_related('department').prefetch_related('achievements').all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.achievements.set(form.cleaned_data['achievements'])
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form, 'title': 'Create Employee'})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            employee.achievements.set(form.cleaned_data['achievements'])
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
        form.fields['achievements'].initial = employee.achievements.all()
    return render(request, 'employees/employee_form.html', {'form': form, 'title': 'Update Employee'})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})