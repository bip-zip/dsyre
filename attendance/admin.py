from django.contrib import admin
from .models import Employee, AttDate, Attendance

admin.site.register(Employee)
admin.site.register(AttDate)
admin.site.register(Attendance)
