from django.views import generic
from django.contrib import messages
from .models import Activity, Task
from django.shortcuts import redirect, HttpResponseRedirect


class PHome(generic.TemplateView):
    template_name = 'phome.html'

    def get_context_data(self, **kwargs):
        context = super(PHome, self).get_context_data(**kwargs) 
        ptopics = Activity.objects.all().order_by('completed').order_by('deadline')
        context.update({'ptopics':ptopics})
        return context
    
class ActivityDetail(generic.DetailView):
    model = Activity
    template_name='activitydetail.html'


    # def get_context_data(self, **kwargs):
    #     context = super(ActivityDetail, self).get_context_data(**kwargs) 
        
    #     context.update({'detail_active':'active','form':form})
    #     return context

def add_activity(request):
    title = request.POST['title']
    deadline = request.POST['deadline']
    activity =Activity.objects.create(title=title, deadline=deadline)
    activity.save()
    return redirect('/progress')

def add_task(request):
    aid = request.POST['activity']
    tid = request.POST['task']
    activity = Activity.objects.get(id=aid)
    title = request.POST['title']
    desc = request.POST['desc']
    step = request.POST['step']
    if Task.objects.filter(id=tid).first():
        task = Task.objects.get(id=tid)
        task.title=title
        task.desc = desc
        task.step = step
        task.save()
    else:
        task =Task.objects.create(activity = activity, title=title, desc=desc, step=step)
        task.save()
    return HttpResponseRedirect('/progress/'+aid)

def mark_completed(request,id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/progress')

def mark_done(request,id):
    activity = Activity.objects.get(id=id)
    activity.completed = True
    activity.save()
    return redirect('/progress')

def delete_task(request,id):
    instance = Task.objects.get(id=id)
    instance.delete()
    messages.success(request,(instance.title)+" has dropped.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))