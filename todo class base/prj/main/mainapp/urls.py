from django.urls import path,include
from .import views
 
urlpatterns = [
    path('a/',views.taskList,name='task'),
    path('c',views.index),
]