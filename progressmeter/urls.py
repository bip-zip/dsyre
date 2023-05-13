from django.urls import path
from . import views
app_name = 'progressmeter'

urlpatterns = [
    path('', views.PHome.as_view()),
    path('add_activity', views.add_activity),
    path('add_task', views.add_task),
    path('<int:pk>/', views.ActivityDetail.as_view(), ),
    path('mark_completed/<int:id>', views.mark_completed),
    path('completed_all/<int:id>', views.mark_done),
    path('delt/<int:id>',views.delete_task),

    
]
