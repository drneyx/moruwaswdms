from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages

# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

def employee_form(request, id=0):
    context = {'employee_list':Employee.objects.all()}
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee= Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee= Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance= employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
        return render(request, 'employee_register/employee_list.html', context)

def employee_delete(request, id):
    employee= Employee.objects.get(pk=id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully!')
    context = {'employee_list':Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

def index(request):
    return render(request, 'employee_register/index.html')


#home page1
def index2(request):
    return render(request, 'employee_register/index2.html')

#login page
def login(request):
    return render(request, 'employee_register/login.html')

#register page
def register(request):
    return render(request, 'employee_register/register.html')

#list of blocks page
def tables(request):
    return render(request, 'employee_register/tables.html')


#about page
def about(request):
    return render(request, 'employee_register/about.html')


#success page
def success(request):
    return render(request, 'employee_register/success.html')


#Admin-assign page
def assign(request):
    return render(request, 'employee_register/assign.html')


#flow rate page
def flow(request):
    return render(request, 'employee_register/flow.html')


#water level for tank1
def Tank1(request):
    return render(request, 'employee_register/Tank1.html')


#Water level for tank2
def Tank2(request):
    return render(request, 'employee_register/Tank2.html')
