from django.shortcuts import render

# Create your views here.
def index(request):
    # Render the HTML template about.html with the data in the context variable
    return render(
        request,
        'events.html',
        context={},
    )