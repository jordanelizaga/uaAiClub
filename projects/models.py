from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.project_name

class Description(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True,)
    project_desc = models.CharField(max_length=140)
    def __str__(self):
        return self.project_desc
    
class BulletinPost(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    post_date = models.DateTimeField('date posted')
    post_user = models.CharField(max_length=35)
    post_message = models.CharField(max_length=140)
    def __str__(self):
        return self.post_message 