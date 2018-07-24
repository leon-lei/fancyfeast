from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from accounts.models import UserProfile
from tribes.models import Event, Tribe

from .forms import EventForm, EventTribeForm, TribeForm


class MyEvents(View):
    template_name = 'tribes/my_events.html'

    def get(self, request):
        chieftain_count = UserProfile.objects.get(user=request.user).chieftain.count()
        my_events = UserProfile.objects.get(user=request.user).event.all()
        return render(request, self.template_name, {'chieftain_count': chieftain_count, 'my_events': my_events})


class MyTribes(View):
    template_name = 'tribes/my_tribes.html'

    def get(self, request):
        my_tribes = UserProfile.objects.get(user=request.user).tribe.all()
        return render(request, self.template_name, {'my_tribes':my_tribes})


class TribeCreate(View):
    form_class = TribeForm
    template_name = 'tribes/create_tribe_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            tribe = form.save(commit=False)
            tribe.name = form.cleaned_data['name']
            tribe.chieftain = UserProfile.objects.get(user=request.user)
            tribe.save()

            # Adds to tribemen M2M field
            tribe.tribesmen.add(UserProfile.objects.get(user=request.user))
            tribe.save()
            return redirect(reverse('tribes:my-tribes'))
        else:
            return render(request, self.template_name, {'form':form})


class TribeDelete(DeleteView):
    model = Tribe
    success_url = reverse_lazy('tribes:my-tribes')


class TribeDetails(DetailView):
    model = Tribe
    template_name = 'tribes/tribe_details.html'


class TribeUpdate(UpdateView):
    model = Tribe
    fields = ['name', 'chieftain', 'description', 'tribesmen', 'image']


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('tribes:my-events')


class EventDetails(DetailView):
    model = Event
    template_name = 'tribes/event_details.html'


class EventUpdate(UpdateView):
    model = Event
    fields = [
        'name', 'description', 'datetime', 
        'street', 'city', 'zipcode', 'state',
        'attendees', 'yes', 'no']


def tribe_leave(request, pk=None):
    if pk:
        tribe = Tribe.objects.get(pk=pk)
        ex_member = UserProfile.objects.get(user=request.user)
        tribe.tribesmen.remove(ex_member)
        tribe.save()
        return redirect(reverse('tribes:my-tribes'))
    else:
        return redirect(reverse('tribes:my-tribes'))

def event_create_pk(request, pk=None):
    if request.method == 'POST':
        form = EventTribeForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.name = form.cleaned_data['name']
            event.datetime = form.cleaned_data['datetime']
            event.tribe = Tribe.objects.get(pk=pk)
            event.save()

            # Adds to attendees M2M field
            event.attendees.add(UserProfile.objects.get(user=request.user))
            event.save()

            return redirect(reverse('tribes:my-events'))
        else:
            return render(request, 'tribes/event_form.html', {'form': form})
    else:
        form = EventTribeForm()
        return render(request, 'tribes/event_form.html', {'form': form})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(user=request.user, data=request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.name = form.cleaned_data['name']
            event.datetime = form.cleaned_data['datetime']
            event.tribe = form.cleaned_data['tribe']
            event.save()

            # Adds to attendees M2M field
            event.attendees.add(UserProfile.objects.get(user=request.user))
            event.save()

            return redirect(reverse('tribes:my-events'))
    else:
        form = EventForm(user=request.user)
    return render(request, 'tribes/event_form.html', {'form': form})

