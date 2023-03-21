from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Note, Register, Profile, Feedback, Booking
from .forms import NoteForm, PostForm
from django.views.generic.edit import CreateView


def home_page(request):
    return render(request, 'index.html')


class PostList(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/all_projects.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        notes = post.note.filter(approved=True).order_by("created_on_note")
        voted = False
        if post.votes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
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
            note = note_form.save(commit=False)
            note.note = post
            note.save()
        else:
            note_form = NoteForm()

        return render(
            request,
            "post_detail.html",
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


class UserProfileEdit(View):

    def user_posts_edit(request):
        return render(request, 'templates/post_user_get.html')


class UserProfileDelete(View):

    def user_posts_delete(request):
        return render(request, 'templates/post_user_get.html')


class UserPostsNone(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


def get_user_posts(request):
    user_posts = Post.objects.all()
    context = {
        'user_posts': user_posts
    }

    return render(request, 'posts/user_posts.html', context)


class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    success_url = '/posts/post_create.html'
    fields = [
        'title',
        'industry',
        'content',
        'post_image',
        'excerpt',
        {'author[1]'}
    ]


class PostUpdate(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class PostDelete(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


def contact_page(request):
    return render(request, 'contact.html')


class FeedbackSend(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class FeedbackResponse(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserBookingCreate(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserBookingView(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserBookingEdit(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserBookingDelete(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')
