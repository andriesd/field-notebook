from django.db import models

# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.place_name

class Creator(models.Model):
    creator_name = models.CharField(max_length=150)
    creator_home = models.ForeignKey(Place)
    
    def __unicode__(self):
        return self.creator_name

class Object(models.Model):
    object_name = models.CharField(max_length=50)
    year_created = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=75, blank=True)
    location_created = models.CharField(max_length= 75, blank = True)
    place_created = models.ForeignKey(Place, blank=True, null=True)
    giver = models.ForeignKey(Creator, related_name="giver", blank = True, null=True)
    receiver = models.ForeignKey(Creator, related_name="receiver", blank = True, null=True)
    object_creator = models.ForeignKey(Creator, blank=True, null=True)
    object_image = models.ImageField(blank = True)
    background_notes = models.TextField(blank = True)
    slug = models.SlugField(blank = False)
    
    def __unicode__(self):
        return self.object_name