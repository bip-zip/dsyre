from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


class Topic(models.Model):
    topic = models.CharField(max_length=1000, null=False)
    conclusion = HTMLField(blank=True)
    unsettled = models.BooleanField(default=True)
    startdate = models.DateField(default=datetime.now)
    enddate = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.topic

    # return wordcount

    @property
    def researches(self):
        data = Research.objects.filter(topic=self)
        return data

    @property
    def orderdedresearches(self):
        data = Research.objects.filter(topic=self).order_by('-id')
        return data

    @property
    def totalWordcount(self):
        data = Research.objects.filter(topic=self)
        wordcount = len(data.content)
        return wordcount



class Research(models.Model):
   
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=False)
    link = models.URLField(blank=True)
    content = models.TextField()
    date = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        topic = Topic.objects.get(id=self.topic.id)
        topic.enddate = self.date
        topic.save()
        super(Research, self).save(*args, **kwargs)

    