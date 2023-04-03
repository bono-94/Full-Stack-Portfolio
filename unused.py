class UserProfileCreate(View):

    def create_user_profile(request):

        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            private = 'private' in request.POST
            Profile.objects.create(first_name=first_name, private=private)

            return redirect('get_user_profile')
        return render(request, 'templates/user_profile_create.html')


def get_user_profile(request):
    information = Profile.objects.all()
    context = {
        'information': information
    }
    return render(request, 'profile/user_profile_view.html')


# path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
# path('accounts/register/', CustomSignupView.as_view(), name='account_register'),


# from allauth.account.views import SignupView
# # class CustomSignupView(SignupView):
#     form_class = CustomSignupForm


# class Register(models.Model):

#     username = models.CharField(max_length=21, blank=False, unique=True)
#     password = models.CharField(max_length=50, blank=False)
#     password_two = models.CharField(max_length=50, blank=False)

#     def __str__(self):
#         return self.username

# ACCOUNT_SIGNUP_FORM_CLASS = 'SignupForm'


path('create-profile', views.ProfileCreate.as_view(), name='create_profile'),
path('profile/', views.view_profile, name='view_profile'),
path('profile/<str:username>/', views.view_profile, name='view_profile'),
path('profile/edit/', views.edit_profile, name='edit_profile'),
path('profile/delete/', views.delete_profile, name='delete_profile'),
path('my-profile/', views.ProfileView.as_view(), name='view_profile'),
