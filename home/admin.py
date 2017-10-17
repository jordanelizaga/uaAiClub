from django.contrib import admin

# Register your models here.
from .models import Newsletter
from .models import Schedule

admin.site.register(Newsletter)
admin.site.register(Schedule)