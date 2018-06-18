from django.db import models
from django.urls import reverse

from accounts.models import UserProfile


class Tribe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='tribe_image', blank=True)
    chieftain = models.ForeignKey(UserProfile, related_name='chieftain', on_delete=models.CASCADE)
    tribesmen = models.ManyToManyField(UserProfile, related_name='tribesmen')

    def get_absolute_url(self):
        return reverse('tribes:tribe-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=80, blank=True)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateField(blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    yes = models.IntegerField(default=0)
    no = models.IntegerField(default=0)
    tribe = models.ForeignKey(Tribe, related_name='tribe', on_delete=models.CASCADE)
    members = models.ManyToManyField(UserProfile, related_name='members')
    
    def get_absolute_url(self):
        return reverse('tribes:event-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('updated',)