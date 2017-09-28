from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .models import Project 
from .forms  import ProjectForm, PostForm 
from datetime import datetime

'''
    Show the detailed project page, after clicking the project hyperlink
    Also, create the "Add a Bulletin Post" form
    Return projectDetail.html
'''
def showProject(request, project_id):
    index = project_id

    # set project to the correct index
    project = Project.objects.get(pk=index)
    
    # if this is a POST request we need to process the form data
    '''
        class BulletinPost(models.Model):
            project = models.ForeignKey(Project, on_delete=models.CASCADE)
            post_date = models.DateTimeField('Date Posted')
            post_user = models.CharField(max_length=35)
            post_message = models.CharField(max_length=140)
    '''
    if request.method == 'POST':
        form = PostForm(request.POST, )
        
        # after clicking "Submit" button, validate form and save to database if ok
        if form.is_valid():
            form.save()
            # refresh the page after submitting
            return HttpResponseRedirect('/projects/' + project_id)

    # if a GET (or any other method) we'll create a blank form
    # if we're creating a webpage, we'll create blank form
    # --Also, because we are hiding project and post_date, we must initialize it.
    # Not initializing it treats it as a null object ""VERY BAD""
    else:
        form = PostForm(initial={ 'project' : project, 'post_date': datetime.now(),}, )
    
    # context allows you to grab variabes from view onto the template.
    context = { 'project' : project, 'form': form }

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'projectDetail.html',
        context,
    )


def index(request):
    # if this is a POST request we need to process the form data
    '''
        ProjectForm() tells us to create a form with the ProjectForm Object
            class Project(models.Model):
            project_name = models.CharField(max_length=50, default="")
            pub_date = models.DateTimeField('Date Created')
            project_desc = models.CharField(max_length=10000, default="")
    '''
    if request.method == 'POST':
        form = ProjectForm(request.POST, )
        # after clicking "Submit" button, validate form and save to database if ok
        if form.is_valid():
            form.save()
            # refresh the page after submitting
            return HttpResponseRedirect('/projects/') 

    # if a GET (or any other method) we'll create a blank form
    # if we're creating a webpage, we'll create blank form
    # --Also, because we are hiding pub_date, we must initialize it.
    # Not initializing it treats it as a null object ""VERY BAD""
    else:
        
        form = ProjectForm(initial={ 'pub_date': datetime.now(),}, )

    # Enumerate all projects in alpha order by 'project name
    project_list = Project.objects.order_by('project_name')

    # context allows you to grab variabes from view onto the template.
    context ={ 'form': form, 'project_list': project_list, } 

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'projects.html',
        context,
    )