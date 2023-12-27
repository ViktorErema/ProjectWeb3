from django import forms
from django.forms import ModelForm

from .models import *



class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name',
                  'age',

                  )

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('name',
                  'number',
                  )

# class ListItemForm2(forms.Form):
#     items_person = forms.ModelChoiceField(queryset=Person.nodes.all())
#
#
# class ListItemForm3(forms.Form):
#     items_car = forms.ModelChoiceField(queryset=Car.nodes.all())