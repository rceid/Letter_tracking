from dal import autocomplete
from .models import Legislator, zip_choices
from django import forms

class LegSearchForm(forms.Form):
    legs = sorted(list(Legislator.objects.all()), key= lambda leg: leg.name)
    leg = forms.MultipleChoiceField(
        label="",
        required=True,
        widget=forms.Select,
        choices=zip_choices(legs)
    )