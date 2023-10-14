from django.shortcuts import render,redirect
from django.views import generic
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages

class Home(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs) 
        today = datetime.today()
        td_topics=Topic.objects.filter(startdate__year=today.year, startdate__month=today.month, startdate__day=today.day)|Topic.objects.filter(enddate__year=today.year, enddate__month=today.month, enddate__day=today.day)
        history = Topic.objects.all().order_by('-startdate')
        unsettled = Topic.objects.filter(unsettled=True)
        context.update({'td_topics':td_topics,'history':history,'unsettled':unsettled,'home_active':'active'})
        return context