
from django.urls import path
from .views import *
urlpatterns = [
    path('', financeHome, name='finance-home' ),
    path('formsubmmit', formSubmit, name='form-submit' ),
   
 ]
 


