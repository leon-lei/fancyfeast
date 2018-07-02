from django import forms

from .models import Tribe


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