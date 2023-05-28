from django import forms
from .models import TaskReminder

class TaskReminderForm(forms.ModelForm):

    class Meta:
        model = TaskReminder
        fields = '__all__'
        widgets = {
            'timedate':forms.TextInput(attrs={'type':'datetime-local'}),
        }
    
