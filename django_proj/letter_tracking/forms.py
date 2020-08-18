from dal import autocomplete
from .models import Legislator
from django import forms


class ItemForm(forms.ModelForm):
    legislator = forms.ModelChoiceField(
        queryset=Legislator.objects.all(),
        widget=autocomplete.ModelSelect2(url='search_form')
    )

    class Meta:
        model = Legislator
        fields = ('__all__')