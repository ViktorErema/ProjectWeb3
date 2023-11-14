from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):

    class Meta:

        model = Document
        fields = (
            'title',
            'text',
        )


class ListItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Document.objects.all())