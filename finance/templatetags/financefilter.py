from django import template
from finance.models import FinanceSheet
import datetime
from django.db.models import F, Sum

register = template.Library()

@register.filter(name='transbydate')
def transByDate(value, statement):
    # today = datetime.date.today()
    data = FinanceSheet.objects.filter(tdate=value, statement=statement)
    return data


@register.filter(name='totaldateprice')
def totalDateprice(value, statement):
    data = FinanceSheet.objects.filter(tdate=value, statement=statement).aggregate(Sum('price'))['price__sum']
    return data


@register.filter(name='totalstatement')
def totalStatement(value):
    data = FinanceSheet.objects.filter(statement=value).aggregate(Sum('price'))['price__sum']
    if data == None:
        return '00.00'
    return data







