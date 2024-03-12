from django import forms

# from .models import Participant
#
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email', 'name']

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')
    name = forms.CharField(label="Your name", max_length=255)