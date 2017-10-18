from django.db import models

from django.forms import ModelForm

# Create your models here.
# e-mail notification model
class Newsletter(models.Model):
    email = models.EmailField(max_length=254)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    def __str__(self):
        return self.email
	
class Schedule(models.Model): 
    date = models.DateField('Date')
    desc = models.TextField('Description',max_length=10000)
    loc = models.CharField('Location',max_length=1000)
    def __str__(self):
        return " Descr.: " + self.desc
		
class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        labels = { 
            "email" : "E-Mail",
            "firstName" : "First Name",
            "lastName" : "Last Name",
        }
        fields = '__all__'