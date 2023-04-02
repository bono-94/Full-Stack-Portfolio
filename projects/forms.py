from .models import Profile, Post, Note, Feedback
from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        return user


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
            'email',
            'bio',
            ]

    profile_image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=21, required=True)
    last_name = forms.CharField(max_length=21, required=True)
    location = forms.CharField(max_length=21, required=True)
    company = forms.CharField(max_length=21, required=True)
    occupation = forms.CharField(max_length=21, required=True)
    email = forms.EmailField(max_length=42)
    bio = forms.CharField(max_length=214)

    def signup(self, user, request):

        user = super(ProfileRegistration, self).save(request)
        user_profile = Profile()
        user_profile.profile_image = self.cleaned_data['profile_image']
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.location = location
        user_profile.company = company
        user_profile.occupation = occupation
        user_profile.email = email
        user_profile.bio = self.cleaned_data['bio']
        user_profile.save()
        return user


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
