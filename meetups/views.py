from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup
from .forms import RegistrationForm

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
        if request.method == 'GET':
            registration_form = RegistrationForm()
          
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                selected_meetup.save()
                return redirect('confirm_registration')
                
        return render(request, 'meetups/meetup-details.html', {
            'meetup': selected_meetup,
            'meetup_found': True,
            'form': registration_form
        })
        
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        } )

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')