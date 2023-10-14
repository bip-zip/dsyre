from django.shortcuts import render, HttpResponse, redirect
from .models import FinanceSheet

from .forms import FinanceSheetForm
from django.http import HttpResponseRedirect


def financeHome(request):
    
    form = FinanceSheetForm
    expenses =  FinanceSheet.objects.filter(statement='expenses').order_by('-tdate').values('tdate').distinct()
    income =  FinanceSheet.objects.filter(statement='income').order_by('-tdate').values('tdate').distinct()
    savings =  FinanceSheet.objects.filter(statement='savings').order_by('-tdate').values('tdate').distinct()
    analytics =analysis()
    return render (request, 'financehome.html',{'expenses':expenses,'income':income,'savings':savings,'form':form, 'analysis':analytics})

def formSubmit(request):
    if request.method == 'POST':
        form = FinanceSheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/finance')
        else:
            return HttpResponse("Something went wrong.")
        
def deleteRecord(request,id):
    fid = FinanceSheet.objects.get(id=id)
    fid.delete()
    return redirect('/finance')


from django.db.models import Sum
from django.db.models.functions import TruncMonth
def analysis():
    totals = FinanceSheet.objects.annotate(
        month=TruncMonth('tdate')
    ).values('month', 'statement').annotate(
        total=Sum('price')
    )

    # Organize the data into a dictionary
    monthly_data = {}
    for entry in totals:
        month = entry['month']
        statement = entry['statement']
        total = entry['total']

        # Convert month to a human-readable format
        formatted_month = month.strftime('%Y - %B ')  # E.g., "September 2023"

        if formatted_month not in monthly_data:
            monthly_data[formatted_month] = {'expenses': 0, 'income': 0, 'savings': 0}

        monthly_data[formatted_month][statement] = total
    return monthly_data

