"""API_company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from OJSC import views
from rest_framework.routers import DefaultRouter
from OJSC.views import get_employees, new_emp

router = DefaultRouter()
# router.register('employees', views.EmployeeCreate)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_employees', get_employees, name ='get_employees'),
    path('api/new_emp', new_emp, name ='new_emp'),
    path('api/', include(router.urls))
]
