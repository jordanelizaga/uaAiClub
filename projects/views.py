from django.shortcuts import render

# Create your views here.
from .models import Project 

def index(request):
    project_list = Project.objects.order_by('-pub_date')[:]
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'projects.html',
        context={ 'project_list': project_list, },
    )