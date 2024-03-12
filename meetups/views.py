from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup, Participant
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
                participant_email = registration_form.cleaned_data['email']
                participant_name = registration_form.cleaned_data['name']
                participant, _ = Participant.objects.get_or_create(email=participant_email, name=participant_name)
                selected_meetup.participants.add(participant)
                selected_meetup.save()
                return redirect('confirm_registration', meetup_slug=meetup_slug)
                
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

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {'meetup': meetup})