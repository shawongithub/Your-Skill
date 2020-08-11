from django.urls import path
from . import views

app_name='vocabulary'
urlpatterns = [
  path('list/', views.WordList.as_view(),name='wordlist'),
  path('addtolist/<int:pk>/', views.AddToMyList, name='addtolist'),
  path('mylist/',views.MyListView, name='mylist'),
  path('worddetail/<int:pk>/',views.WordDetail,name='worddetail'),
]
