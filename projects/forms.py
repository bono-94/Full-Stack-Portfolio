from .models import Profile, Post, Note, Feedback
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User


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
            'industry',
            'company',
            'description',
            'content'
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
