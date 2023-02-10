from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'syrapp'
urlpatterns = [
    path('', views.Home.as_view()),
    path('add_topic',views.add_topic),
    path('update_topic',views.update_topic),
    path('add_research',views.add_research),
    path('openJL',views.openJL),
    path('openDF',views.openDF),
    path('check-settled/<int:id>/<str:status>',views.checkSettled),
    path('delr/<int:id>',views.delete_research),
    path('sdocx/<int:id>',views.saveDocx),
    path('<int:pk>/', views.TopicDetail.as_view(), ),
    path('update-research/<int:pk>',views.UpdateResearch.as_view()),
]
