from django import forms

from accounts.models import UserProfile
from tribes.models import Event, Tribe


class TribeForm(forms.ModelForm):
    class Meta:
        model = Tribe
        fields = ('name', 'description')

    def save(self, commit=True):
        tribe = super(TribeForm, self).save(commit=False)
        if commit:
            tribe.save()
        return tribe


class EventTribeForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'datetime')
    
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'placeholder': '2018-07-17 20:00:00'
        }
    ))

    def save(self, commit=True):
        event = super(EventTribeForm, self).save(commit=False)
        if commit:
            event.save()
        return event


class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        user_profile = UserProfile.objects.get(user=user)
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['tribe'].queryset = Tribe.objects.filter(chieftain=user_profile)
        
    class Meta:
        model = Event
        fields = ('name', 'datetime', 'tribe')

    datetime = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'placeholder': '2018-07-17 20:00:00'
        }
    ))

    def save(self, commit=True):
        event = super(EventForm, self).save(commit=False)
        if commit:
            event.save()
        return event