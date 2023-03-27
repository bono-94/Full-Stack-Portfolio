from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Note, Register, Profile, Feedback
from .forms import ProfileForm, NoteForm, PostForm, FeedbackForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User


def home_page(request):

    if request.method == 'GET':

        return render(request, 'index.html')


class ProfileCreate(CreateView):

    model = Profile
    template_name = 'profile/user_profile_create.html'
    success_url = '/my-profile'

    fields = [
        'profile_title',
        'first_name',
        'last_name',
        'location',
        'company',
        'occupation',
        'email',
        'bio',
    ]

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class ProfileView(DetailView):

    def get(self, request, *args, **kwargs):

        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset)

        return render(
            request,
            "profile/user_profile_view.html",
            {
                "profile": profile,
                "profile_form": ProfileForm()
            },
        )


def profile_detail_view(request):

    context = {}

    context["profile"] = Profile.objects.get(username=request.user)

    return render(request, "profile/user_profile_view.html", context)


class ProfileEdit(UpdateView):

    model = Profile
    template_name = 'profile/user_profile_edit.html'
    success_url = '/my-profile'

    fields = [
        'profile_title',
        'first_name',
        'last_name',
        'location',
        'company',
        'occupation',
        'email',
        'bio',
    ]

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class ProfileDelete(DeleteView):

    model = Profile
    template_name = 'profile/user_profile_delete.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


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
        user_posts = Post.objects.all()
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
        'industry',
        'content',
        'description',
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
