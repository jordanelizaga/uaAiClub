from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField('Title',max_length=500)
	image = models.FileField(null=True, blank=True)
	desc = models.TextField('Description',max_length=10000)
	date = models.DateTimeField('Date and Time')
	def __str__(self):
		return self.title