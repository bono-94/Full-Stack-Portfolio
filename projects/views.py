from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Note, Profile, Request
from .forms import NoteForm, PostForm, RequestForm, ProfileForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from projects.models import *
import psycopg2
import pandas as pd


def final(request):
    users = User.objects.all()
    total_users = User.objects.count()
    total_posts = Post.objects.count()
    total_profiles = Profile.objects.count()
    first_day = 'Monday'
    context = {
        'total_users': total_users,
        'users': users,
        'first_day': first_day,
        'total_posts': total_posts,
        'total_profiles': total_profiles
        }
    return render(request, 'index.html', context)


# def display_column(request):
#     # Fetch all values from the desired column
#     column_values = Profile.objects.values('username')

#     # Pass the column_values to the template
#     context = {'column_values': column_values}
#     return render(request, 'about.html', context)

# def profile_list(request):
#     profiles = Profile.objects.all()
#     usernames = Profile.objects.values_list('username', flat=True).distinct()
#     total_profiles = len(usernames)
#     context = {
#         'total_profiles': total_profiles
#     }
#     return render(request, 'index.html', context)

# 2 problems in 1 problem:
# Not able to display database values such as totals of users or total of posts on the index page, cannot even display a list of only usernames from all values in Profile model or User all auth model. No matter what we tried, we just couldnt get it to work. I have also tried different new ways which you can find on top of the file views.py
# Seeing dataframe of postgresql and maybe even retrieve values as pandas dataframe?
# 12:16 pm
# so second part of the question, or another question or as solution to problem above:
# how can I render and is it even possible to render entire dataframe from postgresql linked to this project? For example if there could be another admin page that reports entire dataframe of entire database. If not, is is possible at least import this dataframe as pandas in my python code so I can filter only unique values with python code and then render them to my templates?
# So this is all the information in detail and I would like to know if both scenarios are actually possible to render total amount of unique users and potentially all their names inside of a table on hmtl templates and if it is indeed possible to import or capture dataframe from postgreSQL because I know how to manipulate dataframe data

def home_page(request):

    if request.method == 'GET':

        return render(request, 'index.html')


@login_required
def view_public_profiles(request, user_profile):

    profile_id = get_object_or_404(Profile, id=user_profile)
    return render(request, 'profile/public_profile_view.html', {'profile_id': profile_id})


@login_required
def user_profile(request):

    profile = get_object_or_404(Profile, username=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/user_profile_view.html', context)


@login_required
def edit_profile(request):

    profile = request.user.user_profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post created successfully.')
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/user_profile_edit.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    else:
        return render(request, 'profile/user_profile_delete.html')


class PostList(ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/all_projects.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
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
        'project_image',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserPosts(ListView):

    model = Post
    template_name = 'posts/user_posts.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user, status=1)
        return queryset.order_by('-created_on')


def about_page(request):

    if request.method == 'GET':

        return render(request, 'about.html')


class SupportRequest(CreateView):

    model = Request
    template_name = 'request/request.html'
    success_url = 'about'
    fields = [
        'name',
        'email',
        'request',
        ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
