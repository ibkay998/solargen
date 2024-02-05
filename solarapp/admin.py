from django.contrib import admin
from .models import Installer, UserProfile

# Register your models here.
admin.site.register(Installer)
admin.site.register(UserProfile)