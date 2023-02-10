from django.forms import ModelForm, Textarea, CharField, Form
from tinymce.widgets import TinyMCE
from .models import Research



class EditorForm(ModelForm):

    content= CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':19}),label='')

    class Meta:
        model = Research
        fields = ('content',)
    
