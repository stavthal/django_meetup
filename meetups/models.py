from django.db import models
from django.utils.text import slugify

# Create your models here.
class Meetup(models.Model): # extends the base class of Model
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField()
    