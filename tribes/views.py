from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from accounts.models import UserProfile
from tribes.models import Event, Tribe

from .forms import TribeForm


class IndexView(ListView):
    template_name = 'tribes/index.html'
    context_object_name = 'all_tribes'

    def get_queryset(self):
        return Tribe.objects.all()


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
            return redirect(reverse('tribes:index'))
        else:
            return render(request, self.template_name, {'form':form})


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
