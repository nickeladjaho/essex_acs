from django.db import models
from django.conf import settings
from django.urls import reverse
from autoslug import AutoSlugField

""""
class Promotion(models.Model):
    
    title = CharField(max_length=125, help_text='Name of the event')
    slug = AutoSlugField(populate_from='title')
    event_description = models.TextField()
    guests = models.TextField(help_text='name of outides attendees', blank=True)

    Does the following fields need to be implemented in sep models?
    #tagline = models.CharField(max_length=80, help_text='short snippet that will be below photo')
    #published_date = models.DateField()
    #or date = models.TextField()
    #promo_photo = models.ImageField(upload_to='uploads/', blank=True)
    #published_date = models.DateField()  
    pass


    def __str__(self):
        # Outputs string of model object.
        return self.title

    def get_absolute_url(self):
        pass

"""