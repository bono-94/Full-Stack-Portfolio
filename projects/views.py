
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Note, Profile, Feedback
from .forms import NoteForm, PostForm, FeedbackForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User


def home_page(request):

    if request.method == 'GET':

        return render(request, 'index.html')


@login_required
def profile(request):
    profile = request.user.user_profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/user_profile_view.html', {'form': form})


# @login_required
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


class PostList(ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/all_projects.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("created_on_note")
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
                "notes": notes,
                "noted": False,
                "voted": voted,
                "note_form": NoteForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("created_on_note")
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        note_form = NoteForm(data=request.POST)

        if note_form.is_valid():
            note_form.instance.email = request.user.email
            note_form.instance.name = request.user.username
            note_form.instance.username = User.objects.get(id=request.user.id)
            note = note_form.save(commit=False)
            note.note = post
            note.save()
        else:
            note_form = NoteForm()

        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
                "note": note,
                "notes": notes,
                "noted": True,
                "voted": voted,
                "note_form": NoteForm()
            },
        )


class PostVote(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.votes.filter(id=request.user.id).exists():
            post.votes.remove(request.user)
        else:
            post.votes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UserPostsNone(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserPosts(View):

    def get_user_posts(request):

        user = request.user
        posts = Post.objects.filter(author=user)
        context = {
            'user_posts': user_posts
        }

        return render(request, 'posts/user_posts.html', context)


class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    success_url = '/my-projects'
    fields = [
        'title',
        'description',
        'industry',
        'company',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class PostDelete(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


def contact_page(request):

    if request.method == 'GET':

        return render(request, 'contact.html')


class FeedbackSend(CreateView):

    model = Feedback
    template_name = 'feedback/feedback.html'
    success_url = ''
    fields = [
        'name',
        'email',
        'feedback'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
