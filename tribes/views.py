from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tribes.models import Event, Tribe

class IndexView(ListView):
    template_name = 'tribes/index.html'
    context_object_name = 'all_tribes'

    def get_queryset(self):
        return Tribe.objects.all()


class TribeCreate(CreateView):
    model = Tribe
    fields = ['name', 'chieftain', 'tribesmen' ,'image']


class TribeDelete(DeleteView):
    model = Tribe
    success_url = reverse_lazy('tribes:index')


class TribeDetails(DetailView):
    model = Tribe
    template_name = 'tribes/tribe_details.html'


class TribeUpdate(UpdateView):
    model = Tribe
    fields = ['name', 'chieftain', 'description', 'tribesmen', 'image']


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'description', 'date', 'tribe']


class EventDetails(DetailView):
    model = Event
    template_name = 'tribes/event_details.html'


class EventUpdate(UpdateView):
    model = Event
    fields = [
        'name', 'description', 'date', 
        'street', 'city', 'zipcode', 'state',
        'members', 'yes', 'no']


class MyEventsIndex(ListView):
    template_name = 'tribes/my_events_index.html'
    context_object_name = 'my_events'

    def get_queryset(self):
        return Event.objects.filter(attending = request.user)  # contains?