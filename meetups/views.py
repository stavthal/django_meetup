from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the meetups index.")
    # Render the index.html template
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })
    
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup': selected_meetup,
            'meetup_found': True
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        } )