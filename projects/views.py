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


# ABOUT PAGE INFO
def final(request):
    users = User.objects.all()
    total_users = User.objects.count()
    total_posts = Post.objects.count()
    total_profiles = Profile.objects.count()
    first_day = 'Monday'
    industry_values = Profile.objects.values_list('industry', flat=True).distinct()
    total_industries = len(industry_values)
    context = {
        'total_users': total_users,
        'users': users,
        'first_day': first_day,
        'total_posts': total_posts,
        'total_profiles': total_profiles,
        'industry_values': industry_values,
        'total_industries': total_industries
        }
    return render(request, 'index.html', context)


def home_page(request):

    if request.method == 'GET':

        return render(request, 'index.html')


def about_page(request):

    if request.method == 'GET':

        return render(request, 'about.html')

# PROFILE
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
            messages.success(request, 'Your profile is updated successfully.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please check all input fields for errors.')
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


# POST
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


class PostDetailDraft(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=0)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/user_post_detail.html",
            {
                "post": post,
                "notes": notes,
                "noted": False,
                "voted": voted,
                "note_form": NoteForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=0)
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
            "posts/user_post_detail.html",
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
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def post_edit(request, post_id):

    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post is updated successfully.')
            return redirect('user_posts')
        else:
            messages.error(request, 'Please check all input fields for errors.')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/user_posts_edit.html', {'form': form})


@login_required
def post_delete(request, post_id):

    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('user_posts')

    else:
        return render(request, 'posts/user_posts_delete.html', {'post': post})


class UserPosts(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_on')


# REQUEST
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
