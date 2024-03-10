from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the meetups index.")
    # Render the index.html template
    meetups = [
        { 'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup' },
        { 'title': 'A Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup' },
        { 'title': 'A Third Meetup', 'location': 'London', 'slug': 'a-third-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
    
def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A First Meetup', 
        'description': 'This is the first meetup!',
        'location': 'New York',
        'image': 'https://images.unsplash.com/photo-1527682497263-6d2e6f24b588'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup': selected_meetup
    })