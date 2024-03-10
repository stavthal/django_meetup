from django.db import models

# Create your models here.
class Meetup(models.Model): # extends the base class of Model
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    