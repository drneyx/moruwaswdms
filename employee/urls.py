"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from employee_register import views

from django.conf import settings
from django.conf.urls.static import static
#from users import views as user_views

router=routers.DefaultRouter()
#router.register('api',views.SensorDataC,base_name='api')
router.register('api',views.SensorDataC)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('employee_register.urls')),
    path('rt/', include(router.urls))
    #user login and registartion
    #path('register/', user_views.register, name='register'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)