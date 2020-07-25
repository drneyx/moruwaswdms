from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import EmployeeForm, CreateUserForm,BlockDetailsForm,TechDetailsForm, UserUpdateForm
from .models import Employee, SensorData,BlockDetails,TechDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from .serializers import SensorDataSerializer

from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.db.models import Avg, Count, Min, Sum
import nexmo




# Create your views here.


class SensorDataC(ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class=SensorDataSerializer


@login_required(login_url='logiin')
@admin_only
def Tank1(request):
    
    sensor = SensorData.objects.all()
    least = SensorData.objects.last()

    labels = ["Height"]
    data1 = [least]
    data = {
             "labels":labels,
             "data1":data1,
            }


    context = {'sensor':sensor,'least':least,'data':data}

    
    return render(request, 'employee_register/Tank1.html', context)

#def sensordata_delete(request,id):
 #   sensordata= SensorData.objects.get(pk=id)
  #  sensordata.delete()
   # messages.success(request, 'Data deleted successfully!')
    #context = {'Tank1':SensorData.objects.all()}
    #return render(request, 'employee_register/Tank1.html', context)



@login_required(login_url='logiin')
@allowed_users(allowed_roles=['admin'])
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

@login_required(login_url='logiin')
@admin_only
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

@login_required(login_url='logiin')
@allowed_users(allowed_roles=['admin'])
def employee_delete(request, id):
    employee= Employee.objects.get(pk=id)
    if request.method == "POST":
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')
    context = {'employee':employee}
    return render(request, 'employee_register/deletee.html', context)




@login_required(login_url='logiin')
@allowed_users(allowed_roles=['admin'])
def Tech_list(request):
    context = {'Tech_list': TechDetails.objects.all()}
    return render(request , 'employee_register/Tech_list.html', context)




@login_required(login_url='logiin')
@allowed_users(allowed_roles=['admin'])
def Tech_delete(request, id):
    employee= TechDetails.objects.get(pk=id)
    if request.method == "POST":
        employee.delete()
        messages.success(request, 'Technician deleted successfully!')
        return redirect('Tech_list')
    context = {'employee':employee}
    return render(request, 'employee_register/delete1.html', context)



def index(request):
    return render(request, 'employee_register/index.html')

@login_required(login_url='logiin')
@allowed_users(allowed_roles=['Technicians'])
def account_setting(request):
   # employee = Employee.objects.create(user = request.user)
    
    employee = request.user.employee
    empo = request.user

    form = EmployeeForm(instance = employee)

    form2 = UserUpdateForm(instance = empo)


    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        form2 = UserUpdateForm(request.POST, instance= empo)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'profile updated successfully!')
            return redirect('profile')

    context = { 'form':form, 'form2':form2}


    return render(request, 'employee_register/account_setting.html',context)



#home page1
@login_required(login_url='logiin')
@admin_only
def index2(request):
    return render(request, 'employee_register/index2.html')

#login page
@unauthenticated_user
def logiin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index2')
        else:
            messages.warning(request, 'Username or password is incorrect')
           
    context= {}
    return render(request, 'employee_register/logiin.html')

#register page
@unauthenticated_user
def register(request):
        form1 = CreateUserForm()
        form3 = EmployeeForm()
        if request.method == 'POST':
            form1 = CreateUserForm(request.POST)
            form3 = EmployeeForm(request.POST)
            if form1.is_valid() and form3.is_valid():
                form3.save()
                user = form1.save() 
                username = form1.cleaned_data.get('username')

                group = Group.objects.get(name='Technicians')
                user.groups.add(group)

                Employee.objects.create(
                    user=user,
                    )

                messages.success(request, 'Account was created for ' + username + ' successfully!')
                return redirect('logiin')
        context = {'form1':form1, 'form3':form3}
        return render(request, 'employee_register/register.html',context )

@unauthenticated_user
def Tech_form(request):

    return render(request, 'employee_register/Tech_form.Html')



#log out

def logoutUser(request):
    logout(request)
    return redirect('logiin')

#list of blocks page
@login_required(login_url='logiin')
@admin_only
def tables(request):

    blocks = BlockDetails.objects.all()


    total_blocks = blocks.count()

    total = blocks.aggregate(Sum('block_av_usage'))

    total_customers = blocks.aggregate(Sum('block_total_customers'))

    context = {'tables':blocks,'total_blocks':total_blocks,'total':total,'total_customers':total_customers }
    return render(request, 'employee_register/tables.html',context)


#about page
def about(request):
    return render(request, 'employee_register/about.html')


#success page
@login_required(login_url='logiin')
def success(request):
    phone = request.POST.get('phone','')
    text = request.POST.get('text','')

    return render(request, 'employee_register/success.html', {'phn':phone, 'txt':text})

#TechUser
@login_required(login_url='logiin')
@allowed_users(allowed_roles=['Technicians'])
def profile(request):
    u_form = UserUpdateForm()
    p_form = EmployeeForm()

    context = {
          'u_form':u_form,
          'p_form':p_form
    }

    return render(request, 'employee_register/profile.html',context)


#Technician profile
@allowed_users(allowed_roles=['Technicians'])
def TechUser1(request):
    form9 = TechDetailsForm()


    if request.method == 'POST':
        form9 = TechDetailsForm(request.POST)
        if form9.is_valid():
            form9.save()
            messages.success(request, 'Successfully uploaded details')
            return redirect('tech_task')



    context = {'form9':form9}

    return render(request, 'employee_register/TechUser.html',context)



#Technician home
@allowed_users(allowed_roles=['Technicians'])
def tech_task(request):
    
    context={'employee_list':Employee.objects.all()}
    return render(request, 'employee_register/tech_task.html',context)



#Admin-assign page
@login_required(login_url='logiin')
def assign(request):
    
    return render(request, 'employee_register/assign.html')


#flow rate page
@login_required(login_url='logiin')
@allowed_users(allowed_roles=['admin'])
def flow(request):

    context = {'employee':Employee.objects.all()}
    return render(request, 'employee_register/flow.html',context)


#water level for tank1
#def Tank1(request):
 #   return render(request, 'employee_register/Tank1.html')


#Water level for tank2
@login_required(login_url='logiin')
@allowed_users(allowed_roles=['admin'])
def Tank2(request):
    form = BlockDetailsForm()

    if request.method == 'POST':
        form = BlockDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Block added successfully!')
            return redirect('tables')



    context = {'form':form}
    return render(request, 'employee_register/Tank2.html',context)


def Tank2_Update(request,id=0):
    blocks = BlockDetails.objects.all()


    total_blocks = blocks.count()
    context = {'tables':blocks,'total_blocks':total_blocks }
    if request.method == "GET":
        if id==0:
            form = BlockDetailsForm()
        else:
            employee= BlockDetails.objects.get(pk=id)
            form = BlockDetailsForm(instance=employee)
        return render(request, 'employee_register/Tank2.html', {'form':form})
    else:
        if id == 0:
            form = BlockDetailsForm(request.POST)
        else:
            employee= BlockDetails.objects.get(pk=id)
            form = BlockDetailsForm(request.POST, instance= employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Block added successfully!')
        return render(request, 'employee_register/tables.html', context)
   

