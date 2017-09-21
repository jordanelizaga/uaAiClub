from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Project 
from .forms  import PostForm 
from datetime import datetime

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, )
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/projects/')

    # if a GET (or any other method) we'll create a blank form
    else:
        # form = PostForm(initial={ 'post_date': datetime.now(), },)
        form = PostForm(initial={ 'post_date': datetime.now(), },)

    project_list = Project.objects.order_by('-pub_date')[:]
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'projects.html',
        context={ 'form': form, 'project_list': project_list, },
    )