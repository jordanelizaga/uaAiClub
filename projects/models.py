from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50, default="")
    pub_date = models.DateTimeField('Date Created')
    project_desc = models.CharField(max_length=10000, default="")
    def __str__(self):
        return self.project_name
    
class BulletinPost(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    post_date = models.DateTimeField('Date Posted')
    post_user = models.CharField('Name', max_length=35)
    post_message = models.CharField('Message', max_length=10000)
    def __str__(self):
        return self.post_message 