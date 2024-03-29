"""
All used views in the application.
Handles user requests and generates responses.
It works in collaboration with models and urls.
It behaves based on users interaction.
All views are defining logic for rendering templates.
They also process form submission.
"""

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Note, Profile
from .forms import NoteForm, PostForm, ProfileForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from projects.models import *
import psycopg2
import pandas as pd
from django.template.loader import render_to_string
from django.http import HttpResponse


# INDEX & ABOUT
def home_page(request):

    if request.method == 'GET':

        return render(request, 'index.html')


def about_page(request):

    if request.method == 'GET':

        total_users = User.objects.count()
        total_posts = Post.objects.count()
        total_industries = Post.objects.values('industry').distinct().count()
        context = {
            'total_users': total_users,
            'total_posts': total_posts,
            'total_industries': total_industries
            }

        return render(request, 'about.html', context)


# PROFILE
@login_required
def view_public_profiles(request, user_profile):

    profile_id = get_object_or_404(Profile, id=user_profile)
    return render(
        request,
        'profile/public_profile_view.html',
        {'profile_id': profile_id}
        )


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
            messages.error(
                request,
                'Please check all input fields for errors.'
                )
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


# POST LISTS
class PostList(ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/public/public_posts_list.html'
    paginate_by = 8


class UserPosts(ListView):
    model = Post
    template_name = 'posts/user/user_posts_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
            ).order_by('-created_on')


# POST DETAILS PUBLISHED
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        post.views += 1
        post.save()
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/public/public_post_details_1_landing.html",
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
            "posts/public/public_post_details_1_landing.html",
            {
                "post": post,
                "note": note,
                "notes": notes,
                "noted": True,
                "voted": voted,
                "note_form": NoteForm()
            },
        )


class PostDetailOpps(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        post.views += 1
        post.save()
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/public/public_post_details_2_opps.html",
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
            "posts/public/public_post_details_2_opps.html",
            {
                "post": post,
                "note": note,
                "notes": notes,
                "noted": True,
                "voted": voted,
                "note_form": NoteForm()
            },
        )


class PostDetailAboutUs(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        post.views += 1
        post.save()
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/public/public_post_details_3_about_us.html",
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
            "posts/public/public_post_details_3_about_us.html",
            {
                "post": post,
                "note": note,
                "notes": notes,
                "noted": True,
                "voted": voted,
                "note_form": NoteForm()
            },
        )


class PostDetailBody(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        post.views += 1
        post.save()
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/public/public_post_details_4_body.html",
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
            "posts/public/public_post_details_4_body.html",
            {
                "post": post,
                "note": note,
                "notes": notes,
                "noted": True,
                "voted": voted,
                "note_form": NoteForm()
            },
        )


class PostDetailFiles(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        post.views += 1
        post.save()
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/public/public_post_details_5_files.html",
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
            "posts/public/public_post_details_5_files.html",
            {
                "post": post,
                "note": note,
                "notes": notes,
                "noted": True,
                "voted": voted,
                "note_form": NoteForm()
            },
        )


class PostDetailProposal(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("-created_on_note")
        post.views += 1
        post.save()
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            voted = True

        return render(
            request,
            "posts/public/public_post_details_6_proposal.html",
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
            "posts/public/public_post_details_6_proposal.html/",
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

        return HttpResponseRedirect(
            reverse(
                'public_post_details_1_landing',
                args=[slug])
            )


class PostCreate(CreateView):
    model = Post
    template_name = 'posts/user/user_post_create.html'
    success_url = '/my-posts'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post is created successfully.')
        return super().form_valid(form)


@login_required
def post_edit(request, post_id):

    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.status = 0
            form.save()
            messages.success(request, 'Your post is updated successfully.')
            return redirect('user_posts_list')
        else:
            messages.error(request, 'Please check all fields for errors.')
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'posts/user/user_post_edit.html',
        {'form': form, 'post': post}
        )


@login_required
def post_delete(request, post_id):

    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect('user_posts_list')

    else:
        return render(
            request,
            'posts/user/user_post_delete.html',
            {'post': post}
            )
