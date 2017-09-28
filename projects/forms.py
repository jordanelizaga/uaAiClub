from django import forms

from .models import Project, BulletinPost

from datetime import datetime

class PostForm(forms.ModelForm):
    class Meta: 
        model = BulletinPost
        fields = ['project', 'post_date', 'post_user', 'post_message' ]
		widgets = {
            'project': forms.HiddenInput(), 
            'post_date': forms.HiddenInput(),
            'post_message' :  forms.Textarea(attrs={'cols': 55, 'rows': 20}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'pub_date': forms.HiddenInput(),
            'project_desc' :  forms.Textarea(attrs={'cols': 55, 'rows': 20}),
        }