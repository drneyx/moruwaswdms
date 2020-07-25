from django.urls import path, include


from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.employee_form,name='employee_insert'), #get and post req fro insert op
    path('<int:id>/', views.employee_form, name='employee_update'), #get and post req for update
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
   # path('delete/<int:id>', views.sensordata_delete, name='sensordata_delete'),
    path('deletTech/<int:id>',views.Tech_delete, name ='Tech_delete'),
    path('<int:id>/',views.TechUser1, name='Tech_update'),
    path('Tech_form', views.Tech_form, name='Tech_form'),
    path('list/', views.employee_list, name='employee_list'), #get req. to retriev and display all records
    path('index/', views.index,  name='index'),
    path('logiin/', views.logiin,  name='logiin'),
    path('logout/', views.logoutUser,  name='logoutUser'),
    path('register/', views.register,  name='register'),
    path('tables/', views.tables,  name='tables'),
    path('about/', views.about,  name='about'),

    path('success/', views.success,  name='success'),
    path('assign/', views.assign,  name='assign'),
    path('flow/', views.flow,  name='flow'),
    path('Tank1/', views.Tank1,  name='Tank1'),
    path('Tank2/', views.Tank2,  name='Tank2'),
    path('Tank2_Update/<int:id>',views.Tank2_Update, name='Tank2_Update'),
    path('index2/', views.index2,  name='index2'),
    path('list2/', views.Tech_list, name = 'Tech_list'),

    path('rest/', include('djoser.urls')),
    path('rest1/', include('djoser.urls.authtoken')),


    path('TechUser/', views.TechUser1, name='TechUser1'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account_setting, name='account_setting'),
    path('tech_task', views.tech_task, name='tech_task'),




    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="employee_register/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="employee_register/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="employee_register/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="employee_register/password_reset_done.html"),name="password_reset_complete"),
   


]
