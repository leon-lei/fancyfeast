from django import forms

from .models import Event, Tribe


class TribeForm(forms.ModelForm):
    class Meta:
        model = Tribe
        fields = ('name', 'description')

    def save(self, commit=True):
        tribe = super(TribeForm, self).save(commit=False)
        # tribe.name = self.cleaned_data['name']

        if commit:
            tribe.save()

        return tribe


class EventForm(forms.ModelForm):
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'placeholder': '2018-07-17 20:00:00'
        }
    ))

    class Meta:
        model = Event
        fields = ('name', 'datetime')

    def save(self, commit=True):
        event = super(EventForm, self).save(commit=False)

        if commit:
            event.save()

        return event
    