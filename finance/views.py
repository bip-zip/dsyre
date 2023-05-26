from django.shortcuts import render, HttpResponse, redirect
from .models import FinanceSheet

from .forms import FinanceSheetForm
from django.http import HttpResponseRedirect


def financeHome(request):
    form = FinanceSheetForm
    expenses =  FinanceSheet.objects.filter(statement='expenses').order_by('-tdate').values('tdate').distinct()
    income =  FinanceSheet.objects.filter(statement='income').order_by('-tdate').values('tdate').distinct()
    savings =  FinanceSheet.objects.filter(statement='savings').order_by('-tdate').values('tdate').distinct()
    return render (request, 'financehome.html',{'expenses':expenses,'income':income,'savings':savings,'form':form})

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
