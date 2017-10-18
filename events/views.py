from django.shortcuts import render

# Create your views here.
from .models import Event

def index(request):
    event_list = Event.objects.order_by('-date')
    context = { 'event_list': event_list, }
    # Render the HTML template about.html with the data in the context variable
    return render(
        request,
        'events.html',
        context,
    )