
from django.contrib import admin
from django.urls import path, include

from . import views


from django.conf import settings 
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='homepage'),
    path('authentication/',include('authentication.urls')),
    path('todo/',include('todo.urls')),
]


urlpatterns+=staticfiles_urlpatterns()