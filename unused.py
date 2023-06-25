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




        # path('my-project/detail', views.user_projects, name='user_project'),
    # path('my-projects/<slug:slug>', views.UserPostDetail().as_view(), name='user_post_detail'),
    # path('vote/<slug:slug>', views.UserPostVote.as_view(), name='vote'),
    # path('my-project/edit', views.edit_project, name='edit_project'),
    # path('my-project/delete/', views.delete_project, name='delete_project'),
    #
    # path('create/', post_create, name='post_create'),
    # path('update/<slug:slug>/', post_update, name='project_update'),
    # path('delete/<slug:slug>/', post_delete, name='post_delete'),
    # path('', post_list, name='post_list'),
    # path('<slug:slug>/', post_detail, name='post_detail'),


    # Views.py explanation of context
    # The key will be what you are going to call the variable in your template
    # The value then points to the Python variable that you plan to send to the template


    # def compute_value():
    # # Compute the value here
    # value = 42
    # return value
# def index(request):
#     # Call the compute_value function to get the computed value
#     value = compute_value()
#     # Render the value in the HTML template
#     return render(request, 'index.html', {'value': value})

# def usernames(request):
#     usernames = User.objects.values_list('username', flat=True)
#     # Pass the usernames value to the context dictionary and render the usernames page
#     context = {'usernames': usernames}
#     return render(request, 'index.html', context)


# def dataframe(request):
#     # Retrieve data from the database
#     data = Profile().objects.all().values()

#     # Convert the data to a pandas dataframe
#     df = pd.DataFrame.from_records(data)

#     # Pass the dataframe to the context dictionary and render the dataframe page
#     context = {'df': df.to_html()}
#     print(f"df:{df}")
#     return render(request, 'index.html', context)


# def retrieve_dataframe(request):
#     # Connect to PostgreSQL database
#     conn = psycopg2.connect(
#         dbname='plsyeoge',
#         user='plsyeoge',
#         password='X,
#         host='Y',
#         port='Z'
#     )

#     # Create a cursor to interact with the database
#     cursor = conn.cursor()

#     # Execute a SQL query to retrieve data
#     cursor.execute('SELECT * FROM projects_profil')

#     # Fetch all rows of data
#     rows = cursor.fetchall()

#     # Close the cursor and connection
#     cursor.close()
#     conn.close()

#     # Convert the data to a Pandas DataFrame
#     df = pd.DataFrame(rows)

#     # You can now manipulate the DataFrame as needed
#     # For example, you can filter unique values
#     unique_users = df['username'].unique()

#     # Pass the data to the template context
#     context = {'unique_users': unique_users, 'df': df}
#     return render(request, 'index.html', context)

# 2 problems in 1 problem:
# Not able to display database values such as totals of users or total of posts on the index page, 
# cannot even display a list of only usernames from all values in Profile model or User all auth model. 
# No matter what we tried, we just couldnt get it to work. I have also tried different new ways which you can find on top of the file views.py

# Seeing dataframe of postgresql and maybe even retrieve values as pandas dataframe?
# 12:16 pm
# so second part of the question, or another question or as solution to problem above:
# how can I render and is it even possible to render entire dataframe from postgresql linked to this project? 
# For example if there could be another admin page that reports entire dataframe of entire database. 
# If not, is is possible at least import this dataframe as pandas in my python code so I can filter only unique values with python code and then render them to my templates?

# So this is all the information in detail and I would like to know if both scenarios are actually possible to render total amount of unique users and potentially
#  all their names inside of a table on hmtl templates and if it is indeed possible to import or capture dataframe from postgreSQL because I know how to manipulate
#  dataframe data



#    {% comment %}



#     <!-- <hr>
#     <div class="container mt-4">
#       <div class="row">
#         <div class="col-md-12">
#           <h1>{{ post.title }}</h1>
#           <p>{{ post.content }}</p>
#           <p>Author: <a href="{% url 'public_profile' profile_id %}">{{ profile_id }}</a></p>
#           Add any other post information you want to display here 
#           <a href="{% url 'public_profile' profile_id %}" class="btn btn-primary">View Author Profile</a>
#         </div>
#       </div>
#     </div>
    
#     <a href="{% url 'public_profile' profile_id %}">
#       Tejst
#     </a>
    
#     <hr>
    
#     <hr>
    
#      <hr> -->

#      {% endcomment %}

    TYPE_OF_FEE_MODEL = (
        ('One-time Fee', 'One-time Fee'),
        ('Percentage', 'Percentage'),
    )


    # PAGE 9
    # POST EVENT
    event_privacy = models.BooleanField(default=False)
    event_color = models.CharField(
        max_length=7,
        default='#ffc107',
        blank=True,
        null=True
    )
    event_image = models.ImageField(
        upload_to='post_event_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )
    event_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='Event URL'
    )
    event_title = models.CharField(max_length=84, blank=True, null=True)
    event_host = models.CharField(max_length=42, blank=True, null=True)
    event_content = models.TextField(max_length=420, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_hour = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], null=True, blank=True)
    event_minute = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)], null=True, blank=True)
    event_location = models.CharField(max_length=42, blank=True, null=True)
    event_price = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999)], null=True, blank=True)
    event_price_cents = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True, blank=True)
    event_capacity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)], null=True, blank=True)

    rspv_yes = models.ManyToManyField(User, related_name="rspv_yes", blank=True)
    rspv_no = models.ManyToManyField(User, related_name="rspv_no", blank=True)
    rspv_maybe = models.ManyToManyField(User, related_name="rspv_maybe", blank=True)
    rspv_next_time = models.ManyToManyField(User, related_name="rspv_next_time", blank=True)

        # PAGE 10
    # POST RESULTS
    post_results_privacy = models.BooleanField(default=False)
    number_of_phases = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)], null=True, blank=True)

    amount_asked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999999)], null=True, blank=True)
    amount_collected = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999999)], null=True, blank=True)

    ownership_offered = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    ownerhip_given = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    team_positions_offered = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21042004)], null=True, blank=True)
    team_positions_given = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21042004)], null=True, blank=True)


    post_colors_list = models.BooleanField(default=False)
    post_color_primary = models.CharField(
        max_length=7,
        default='#292b2c',
    )
    post_color_secondary = models.CharField(
        max_length=7,
        default='#ffc107',
    )
    post_color_text = models.CharField(
        max_length=7,
        default='#000000',
    )


    # COUNTING OF EVENT RSPVS

    def number_of_rspv_yes(self):
        return self.rspv_yes.count()

    def number_of_rspv_no(self):
        return self.rspv_no.count()

    def number_of_rspv_maybe(self):
        return self.rspv_maybe.count()

    def number_of_rspv_next_time(self):
        return self.rspv_next_time.count()