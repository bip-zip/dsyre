from django.shortcuts import render, HttpResponse, redirect
from .models import TaskReminder
from .forms import TaskReminderForm
from django.utils.timezone import datetime
def home(request):
    form = TaskReminderForm
    today = datetime.today()
    today_reminder = TaskReminder.objects.filter(timedate__year=today.year, timedate__month=today.month, timedate__day=today.day).order_by('priority')
    future_reminder = TaskReminder.objects.filter(timedate__year__gte=today.year, timedate__month__gte=today.month, timedate__day__gte=today.day).order_by('priority')
    past_reminder = TaskReminder.objects.filter(timedate__year__lte=today.year, timedate__month__lte=today.month, timedate__day__lte=today.day).order_by('priority')
    context={
        'form':form,
        'today_reminder':today_reminder,
        'future_reminder':future_reminder,
        'past_reminder':past_reminder

        }
    return render(request,'reminder-home.html', context)

def formSubmit(request):
    if request.method == 'POST':
        form = TaskReminderForm(request.POST)
        if form.is_valid():
            form.save()
            # email part
            return redirect('/reminder')
        else:
            return HttpResponse("Something went wrong.")

def deleteTask(request,id):
    tid = TaskReminder.objects.get(id=id)
    tid.delete()
    return redirect('/reminder')
