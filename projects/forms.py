from .models import Profile, Post, Note, Feedback
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User


# class CustomSignupForm(SignupForm):

#     class Meta:
#         model = User
#         fields = [
#             'profile_image',
#             'username',
#             'first_name',
#             'last_name',
#             'location',
#             'company',
#             'occupation',
#             'email',
#             'bio',
#             ]

#     username = forms.CharField(required=True)
#     profile_image = forms.ImageField(required=False)
#     first_name = forms.CharField(max_length=21, required=True)
#     last_name = forms.CharField(max_length=21, required=True)
#     location = forms.CharField(max_length=21, required=True)
#     company = forms.CharField(max_length=21, required=True)
#     occupation = forms.CharField(max_length=21, required=True)
#     email = forms.EmailField(max_length=42, required=True)
#     bio = forms.CharField(max_length=214)

#     def save(self, user, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.profile_image = self.cleaned_data['profile_image']
#         user.username = self.cleaned_data.get('username')
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.location = self.cleaned_data.get('location')
#         user.company = self.cleaned_data.get('company')
#         user.occupation = self.cleaned_data.get('occupation')
#         user.email = self.cleaned_data.get('email')
#         user.bio = self.cleaned_data['bio']
#         user.save(request)
#         return user


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
