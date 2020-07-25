from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee,TechDetails,BlockDetails



class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position','profile_pic')
        labels = {
            'fullname':'Full Name',
            'mobile':'Phone Number',
            'emp_code':'Employee Code',
            'position':'Department',
            'profile_pic':'Profile Picture'
        }



    def __init__(self,  *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
      #  self.fields['position'].empty_label = "select"
        self.fields['emp_code'].required = True
        


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model =  User
        fields = ['username', 'email','password1','password2']
        labels = {
             'username':'Username',
             'email':'Email Address',
             'password1':'password',
             'password2':'Confirm password'
        }

class UserUpdateForm(forms.ModelForm):


    class Meta:
        model =  User
        fields = ['username','email']
        labels = {
            'username':'username',
            'email':'Email'
        }




class BlockDetailsForm(ModelForm):
  class Meta:
    model = BlockDetails
    fields = '__all__'



class TechDetailsForm(forms.ModelForm):
  class Meta:
    model = TechDetails
    fields = ('name', 'phone', 'status')
    labels = {
        'name':'Full Name',
        'phone':'Phone Number',
        'status':'status',
        
        
    }
    def __init__(self,  *args, **kwargs):
        super(TechDetailsForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "select"
        

    