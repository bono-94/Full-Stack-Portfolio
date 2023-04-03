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


# The advantage of having a separate Profile model, as you do, is that you can add additional fields
# to the 'User' without actually messing with the base User model (which can be a nightmare).
# So long as there's a OneToOne relationship between User and Profile (as there is) you can always get ANY
#  information from either of them via the related name or field itself (user_profile and username)

# I will say that because you've got certain views written already, you might meet errors along the way,
# so just be prepared to perhaps delete existing users that might be tripping your old logic up.

class CustomSignupForm(SignupForm):

    class Meta:
        model = User
        fields = [
            'profile_image',
            'username',
            'first_name',
            'last_name',
            'location',
            'company',
            'occupation',
            'email',
            'bio',
            ]

    username = forms.CharField(required=True)
    profile_image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=21, required=True)
    last_name = forms.CharField(max_length=21, required=True)
    location = forms.CharField(max_length=21, required=True)
    company = forms.CharField(max_length=21, required=True)
    occupation = forms.CharField(max_length=21, required=True)
    email = forms.EmailField(max_length=42, required=True)
    bio = forms.CharField(max_length=214)

    def save(self, user, request):
        user = super(CustomSignupForm, self).save(request)
        user.profile_image = self.cleaned_data['profile_image']
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.location = self.cleaned_data.get('location')
        user.company = self.cleaned_data.get('company')
        user.occupation = self.cleaned_data.get('occupation')
        user.email = self.cleaned_data.get('email')
        user.bio = self.cleaned_data['bio']
        user.save(request)
        return user


# class MyUserAdmin(UserAdmin):

#     list_display = ('username', 'email', 'first_name', 'last_name')
#     search_fields = ['username', 'email', 'first_name', 'last_name', 'location', 'occupation', 'company']
#     list_filter = ('username', 'email', 'first_name', 'last_name')
#     summernote_fields = ('bio')


# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)
