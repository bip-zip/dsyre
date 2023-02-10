from django.shortcuts import render,redirect
from django.views import generic
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Attendance, AttDate
class AHome(generic.TemplateView):
    template_name = 'ahome.html'

    def get_context_data(self, **kwargs):
        context = super(AHome, self).get_context_data(**kwargs) 
        attendance = AttDate.objects.all().order_by('-id')
        context.update({'attendance':attendance})
        return context
    