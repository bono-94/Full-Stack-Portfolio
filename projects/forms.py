from .models import Note, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'industry',
            'content',
            'excerpt',
            ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'content_note',
            ]
