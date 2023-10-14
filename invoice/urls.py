
from django.urls import path
from .views import *

app_name=''

urlpatterns = [
    path('', financeHome, name='finance-home' ),
 ]
 


