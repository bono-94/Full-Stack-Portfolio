from django import forms
from .models import Profile, Post, Note, Feedback


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'first_name',
            'last_name',
            'location',
            'company',
            'occupation',
            'bio',
            ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'company',
            'industry',
            'content',
            ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'content_note',
            ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'email',
            'feedback',
            ]
