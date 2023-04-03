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