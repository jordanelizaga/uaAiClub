from django import forms

from .models import Project, BulletinPost

from datetime import datetime

class PostForm(forms.ModelForm):
    class Meta: 
        model = BulletinPost
        fields = ['project', 'post_date', 'post_user', 'post_message' ]
        widgets = {'post_date': forms.HiddenInput()}
    # project = forms.ModelChoiceField(queryset= Project.objects.all())
    # post_date = forms.DateTimeField(label='Date Posted', initial=datetime.now(), )
    # post_user = forms.CharField(max_length=35)
    # post_message = forms.CharField(max_length=140)