from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
# from .models import Book, Author, BookInstance, Genre
from .models import NewsletterForm
from .models import Schedule

def index(request):
    # Render the HTML template index.html with the data in the context variable
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewsletterForm(request.POST,)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request, 'thankYou.html', context={})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewsletterForm()
    
    schedule_list = Schedule.objects.order_by('date')
    context = { 'emailForm' : form, 'schedule_list': schedule_list, }
    return render(
        request,
        'index.html',
        context,
    )