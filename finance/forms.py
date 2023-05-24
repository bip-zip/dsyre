from django import forms
from .models import FinanceSheet

class FinanceSheetForm(forms.ModelForm):

    class Meta:
        model = FinanceSheet
        fields = '__all__'
        widgets = {
            'tdate': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
