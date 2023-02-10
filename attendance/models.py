from django.db import models
from datetime import datetime

class Employee(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AttDate(models.Model):
    date = models.DateField(default=datetime.now)
    occassion = models.CharField(max_length=50)
    regular = models.BooleanField(default=True)

    def __str__(self):
        return '{} - {}'.format(self.date, self.occassion)

    @property
    def attendances(self):
        data = Attendance.objects.filter(date=self.id)
        return data


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.ForeignKey(AttDate, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    arrival= models.CharField(max_length=5)
    depature= models.CharField(max_length=5)
    reason = models.CharField(max_length=500, null=True, blank =True )
    noticed = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.date, self.employee.name)



