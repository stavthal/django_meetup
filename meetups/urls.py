from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index), # our-domain.com/meetups
    path('meetups/success', views.confirm_registration, name='confirm_registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name="meetup-details") # our-domain.com/meetups/a-first-meetup
]
