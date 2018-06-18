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
    fields = ['name', 'chieftain', 'image']


class TribeDelete(DeleteView):
    model = Tribe
    success_url = reverse_lazy('tribes:index')


class TribeDetail(DetailView):
    model = Tribe
    template_name = 'tribes/tribe_detail.html'


class TribeUpdate(UpdateView):
    model = Tribe
    fields = ['name', 'chieftain', 'image']
