from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import NoteForm


class PostList(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
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


class ExampleReturns(View):

    def example_one(request):
        return HttpResponse("<h1>Title</h1><h2>subtitle</h2>")


class UserProfileCreate(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserProfile(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserProfileEdit(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class UserPostsNone(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class PostCreate(View):

    def create_posts(request):
        return render(request, 'templates/post_create.html')


class UserPosts(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class PostUpdate(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


class PostDelete(View):

    def get_user_posts(request):
        return render(request, 'templates/post_user_get.html')


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