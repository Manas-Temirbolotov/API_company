
from django.db import models
from django.utils import timezone




class Title(models.Model):
    title = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Employee(models.Model):
    name = models.CharField(max_length=20)
    date_birth = models.DateField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f' {self.employee.name} - {self.title.title}'



