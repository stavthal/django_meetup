from django.db import models
from django.utils.text import slugify

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name} ({self.address})'
    
class Participant(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.email
    
class Meetup(models.Model): # extends the base class of Model
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    
    def __str__ (self):
        return f'{self.title} - {self.slug}'
    

