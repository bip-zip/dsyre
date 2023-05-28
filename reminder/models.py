from django.db import models

class TaskReminder(models.Model):
    STATUS_CHOICES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    )

    timedate = models.DateTimeField("Date & Time")
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, default='N/A')
    priority = models.CharField('Priority', max_length=10, choices=STATUS_CHOICES, default='medium')
    email = models.EmailField(null=True)

    
    def __str__(self):
        return self.title