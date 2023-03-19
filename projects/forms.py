from .models import Note, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'industry', 'author', 'content', 'post_image', 'excerpt',]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('content_note',)
