from .models import Note, Post, Profile, Feedback
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'industry',
            'content',
            'description',
            ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'content_note',
            ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_title',
            'first_name',
            'last_name',
            'location',
            'company',
            'occupation',
            'email',
            'bio',
            ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'email',
            'feedback',
            ]
