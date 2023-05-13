from django.db import models
from datetime import datetime


class Activity(models.Model):
    title = models.CharField(max_length=200, null=False)
    start_date = models.DateField(default=datetime.now)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Activities'

    @property
    def orderdedtasks(self):
        data = Task.objects.filter(activity=self).order_by('-step')
        return data
    
    @property
    def completedstep(self):
        total = Task.objects.filter(activity=self).count()
        completed = Task.objects.filter(activity=self,completed=True).count()
        return '{}/{}'.format(completed,total)
    
    @property
    def completed_percentage(self):
        total = Task.objects.filter(activity=self).count()
        completed = Task.objects.filter(activity=self,completed=True).count()
        if total==0:
            percentage = 0
        else:
            percentage = (completed/total)*100
        return round(percentage)
    
    @property
    def remaining_days(self):
        remaining = (self.deadline-datetime.now().date()).days
        return remaining
    
    @property
    def next_task(self):
        data = Task.objects.filter(activity=self,completed=False).order_by('step').first()
        return data
    
    

class Task(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    step = models.PositiveIntegerField()
    desc = models.TextField(null=True, blank =True )
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    


    



