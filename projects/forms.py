from django import forms
from .models import Profile, Post, Note, Request


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_color',
            'profile_image',
            'first_name',
            'last_name',
            'location',
            'company',
            'occupation',
            'bio',
        ]
        widgets = {
            'profile_color': forms.TextInput(attrs={'type': 'color'}), # specify the input type as 'color'
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'project_image',
            'title',
            'description',
            'industry',
            'company',
            'content',
        ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'content_note',
        ]


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'name',
            'email',
            'request',
        ]
