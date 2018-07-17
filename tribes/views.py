from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from accounts.models import UserProfile
from tribes.models import Event, Tribe

from .forms import EventForm, TribeForm


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


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'description', 'date', 'tribe']


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('tribes:my-events-index')


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
        return Event.objects.all()  # contains?


def tribe_leave(request, pk=None):
    if pk:
        tribe = Tribe.objects.get(pk=pk)
        ex_member = UserProfile.objects.get(user=request.user)
        tribe.tribesmen.remove(ex_member)
        tribe.save()
        return redirect(reverse('tribes:my-tribes'))
    else:
        return redirect(reverse('tribes:my-tribes'))

def create_event_pk(request, pk=None):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.name = form.cleaned_data['name']
            event.datetime = form.cleaned_data['datetime']
            event.tribe = Tribe.objects.get(pk=pk)
            event.save()

            # Adds to attendees M2M field
            event.attendees.add(UserProfile.objects.get(user=request.user))
            event.save()
            return redirect(reverse('tribes:my-events-index'))
        else:
            # Currently thrown by datetime being incorrect
            return HttpResponse('Form was not valid')
    else:
        form = EventForm()
        args = {'form': form}
        return render(request, 'tribes/event_form.html', args)
