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


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

#                                     VIEWS

# _______________________________________________________________________________________|

# # @login_required
# def profile(request):
#     user_profile = Profile.objects.get_or_create(user=request.username)
#     return render(request, 'profile/user_profile_create.html', {'user_profile': user_profile})

# @login_required
# def view_profile(request):

#     user_profile = get_object_or_404(User, username=request.user.username)

#     return render(request, 'profile/user_profile_view.html', {'user_profile': user_profile})


# @login_required
# def edit_profile(request):

#     # user_profile = get_object_or_404(Profile, user=request.user)
#     try:
#         user_profile = User.objects.get(user=request.user)
#     except User.DoesNotExist:
#         user_profile = None

#     if request.method == 'POST':
#         form = CustomSignupForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('view_profile')
#     else:
#         form = CustomSignupForm(instance=user_profile)

#     return render(request, 'profile/user_profile_edit.html', {'form': form})


# @login_required
# def delete_profile(request):

#     user_profile = get_object_or_404(User, user=request.user)
#     user_profile.delete()
#     return redirect('home')

# class ProfileCreate(CreateView):

#     model = Profile
#     template_name = 'profile/user_profile_create.html'
#     success_url = '/my-profile/'

#     fields = [
#         'profile_title',
#         'first_name',
#         'last_name',
#         'location',
#         'company',
#         'occupation',
#         'email',
#         'bio',
#     ]

#     def form_valid(self, form):
#         form.instance.username = self.request.user
#         return super().form_valid(form)


# class ProfileView(DetailView):

#     def get(self, request, *args, **kwargs):

#         queryset = Profile.objects.filter(user=request.username)
#         profile = get_object_or_404(queryset)

#         return render(
#             request,
#             "profile/user_profile_view.html",
#             {
#                 "profile": profile,
#                 "profile_form": CustomSignupForm()
#             },
#         )
# def profile_detail_view(request):

#     context = {}

#     context["profile"] = Profile.objects.get(username=request.user)

#     return render(request, "profile/user_profile_view.html", context)
# class ProfileEdit(UpdateView):

#     model = Profile
#     template_name = 'profile/user_profile_edit.html'
#     success_url = '/my-profile'

#     fields = [
#         'profile_title',
#         'first_name',
#         'last_name',
#         'location',
#         'company',
#         'occupation',
#         'email',
#         'bio',
#     ]

#     def form_valid(self, form):
#         form.instance.username = self.request.user
#         return super().form_valid(form)


# class ProfileDelete(DeleteView):

#     model = Profile
#     template_name = 'profile/user_profile_delete.html'
#     success_url = '/'

#     def form_valid(self, form):
#         form.instance.username = self.request.user
#         return super().form_valid(form)


# class UserProfileCreate(View):

#     def create_user_profile(request):

#         if request.method == 'POST':
#             first_name = request.POST.get('first_name')
#             private = 'private' in request.POST
#             Profile.objects.create(first_name=first_name, private=private)

#             return redirect('get_user_profile')
# #         return render(request, 'templates/user_profile_create.html')


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

#                                     VIEWS - END

# _______________________________________________________________________________________|

# from allauth.account.forms import SignupForm
# # from django.contrib.auth.models import User
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     print('Signal fired on creation of User')
#     print('Created? ', created)
#     if created:
#         Profile.objects.create(username=instance)
#         try:
#             instance.user_profile.save()
#             print('Do we have a profile created? ', instance.user_profile)
#         except Exception as e:
#             print('No profile related to User')

#     print(create_or_update_user_profile)



















# @login_required
# def project_update(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     if post.author != request.user:
#         messages.error(request, 'You do not have permission to update this post.')
#         return redirect('contact', slug=post.slug)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Blog post updated successfully.')
#             return redirect('contact', slug=post.slug)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'posts/user_posts_edit.html', {'form': form})


# @login_required
# def project_delete(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     if post.author != request.user:
#         messages.error(request, 'You do not have permission to delete this post.')
#         return redirect('user_projects', slug=post.slug)
#     post.delete()
#     messages.success(request, 'Blog post deleted successfully.')
#     return redirect('user_projects')

# @login_required
# def post_list(request):
#     posts = Post.objects.filter(status=1)
#     return render(request, 'contact.html', {'posts': posts})

# @login_required
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'contact.html', {'post': post})


# # class UserPostDetail(View):

# #     def get(self, request, slug, *args, **kwargs):

# #         queryset = Post.objects.filter(status=[1, 0])

# #         post = get_object_or_404(queryset, slug=slug)
# #         notes = post.note.order_by("created_on_note")
# #         voted = False
# #         if post.votes.filter(id=self.request.user.id).exists():
# #             voted = True

# #         return render(
# #             request,
# #             "posts/user_post_detail.html",
# #             {
# #                 "post": post,
# #                 "notes": notes,
# #                 "noted": False,
# #                 "voted": voted,
# #                 "note_form": NoteForm()
# #             },
# #         )


# # class UserPostVote(View):

# #     def post(self, request, slug):
# # #         post = get_object_or_404(Post, slug=slug)

# # #         if post.votes.filter(id=request.user.id).exists():
# # #             post.votes.remove(request.user)
# # #         else:
# #             post.votes.add(request.user)

# #         return HttpResponseRedirect(reverse('user_post_detail', args=[slug]))


# @login_required
# def user_projects(request):

#     project = get_object_or_404(Post, username=request.user)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('user_project')
#     else:
#         form = PostForm(instance=project)

#     context = {
#         'form': form,
#         'project': project
#     }

#     return render(request, 'posts/user_post_detail.html', context)


# @login_required
# def edit_profile(request):

#     profile = request.user.user_profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Blog post created successfully.')
#             return redirect('user_profile')
#     else:
#         form = ProfileForm(instance=profile)
#     return render(request, 'profile/user_profile_edit.html', {'form': form})


# @login_required
# def delete_profile(request):
#     if request.method == 'POST':
#         user = request.user
#         user.delete()
#         return redirect('home')
#     else:
#         return render(request, 'profile/user_profile_delete.html')




    # def get_context_data(self, **kwargs):
    #     context = super(PostList, self).get_context_data(**kwargs)
    #     pk = self.kwargs.get('pk')
    #     if pk:
    #         context['notes'] = Note.objects.filter(note=pk)
    #     return context