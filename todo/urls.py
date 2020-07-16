
from django.urls import path

from . import views

app_name='todo'
urlpatterns = [
   path('list/',views.List, name='list'),
   path('create/',views.create, name='create'),
   path('update/<int:pk>/',views.update,name='update'),
   path('delete/<int:pk>/',views.delete,name='delete'),
]
