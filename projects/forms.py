from django import forms

from .models import Project

from datetime import datetime

class PostForm(forms.Form):
    project = forms.ModelChoiceField(queryset= Project.objects.all())
    post_date = forms.DateTimeField(label='Date Posted', initial=datetime.now(), )
    post_user = forms.CharField(max_length=35)
    post_message = forms.CharField(max_length=140)