from django import forms

from .models import Newsletter

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'