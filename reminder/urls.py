from django.urls import path
from . import views
app_name='reminder'

urlpatterns = [
    path('',views.home,name='home'),
    path('formsubmmit', views.formSubmit, name='form-submit' ),
    path('<id>/delete-task', views.deleteTask, name='delete-task' ),


]
