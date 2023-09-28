from django.contrib import admin
from django.urls import path

from robots.views import RobotAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', RobotAPIView.as_view())
]
