from django.contrib import admin

# Register your models here.
from .models import Project, BulletinPost

admin.site.register(Project)
admin.site.register(BulletinPost)