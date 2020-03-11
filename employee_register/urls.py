from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.employee_form,name='employee_insert'), #get and post req fro insert op
    path('<int:id>/', views.employee_form, name='employee_update'), #get and post req for update
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'), #get req. to retriev and display all records
    path('index/', views.index,  name='index'),
    path('login/', views.login,  name='login'),
    path('register/', views.register,  name='register'),
    path('tables/', views.tables,  name='tables'),
    path('about/', views.about,  name='about'),
    path('success/', views.success,  name='success'),
    path('assign/', views.assign,  name='assign'),
    path('flow/', views.flow,  name='flow'),
    path('Tank1/', views.Tank1,  name='Tank1'),
    path('Tank2/', views.Tank2,  name='Tank2'),
    path('index2/', views.index2,  name='index2'),

]
