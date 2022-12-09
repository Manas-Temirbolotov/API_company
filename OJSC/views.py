import data as data
from django.shortcuts import render

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework import viewsets
from .models import Title, Employee
from .serializers import TitleSerializer, EmployeeSerializer


class TitleNameCreate(generics.CreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class EmployeeNameCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def get_employees(request):
    # emps = Employee.objects.all()
    # context = {
    #     'emps': emps,
    # }
    return HttpResponse(f'Вы находитесь на странице для просмотра')


def new_emp(request):
    name = request.GET.get('name')
    value = request.GET.get('value')
    emp_name = Employee.object.get(name=name)
    emp = Employee.object.create(title=emp_name)
    obj = {'title': emp.employee.name, 'value': emp.employee}
    return HttpResponse(json.dumps(obj))
