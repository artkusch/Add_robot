from django.contrib import admin
from django.urls import path

from robots.views import create_robot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', create_robot)
]
