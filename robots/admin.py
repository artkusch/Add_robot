from django.contrib import admin
from .models import Robot
from import_export import resources

admin.site.register(Robot)