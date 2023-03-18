from .models import Note
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('content_note',)
