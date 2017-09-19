from django.shortcuts import render

# Create your views here.
# from .models import Book, Author, BookInstance, Genre

def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )