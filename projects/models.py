from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):

    title = models.CharField(max_length=210, unique=True)
    industry = models.CharField(max_length=50)
    slug = models.SlugField(max_length=210, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(unique=True)
    post_image = models.ImageField(upload_to=None, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    votes = models.ManyToManyField(User, related_name="projects_votes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_votes(self):
        return self.votes.count()


class Note(models.Model):

    note = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='note')
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=21, null=False, unique=True)
    email = models.EmailField(blank=True)
    content_note = models.TextField()
    created_on_note = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on_note']

    def __str__(self):
        return f"Note {self.content_note} by {self.name}"


class Register(models.Model):

    username = models.CharField(max_length=21, null=False, blank=False, unique=True)
    password = models.PasswordField(max_length=50, null=False, blank=False)
    password_two = models.PasswordField(max_length=50, null=False, blank=False)


class Profile(models.Model):

    slug = models.SlugField(max_length=21, unique=True)
    profile_title = models.CharField(max_length=42, unique=True)
    user_image = CloudinaryField('image', default='placeholder')
    private = models.BooleanField(null=False, blank=False, default=False)
    username = models.CharField(max_length=21, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=21, null=False, blank=False)
    last_name = models.CharField(max_length=21, null=False, blank=False)
    location = models.CharField(max_length=21, null=False, blank=False)
    company = models.CharField(max_length=21, null=False, blank=False)
    occupation = models.CharField(max_length=21, null=False, blank=False)
    email = models.EmailField(max_length=42, unique=True)
    bio = models.TextField(max_length=214)


class Feedback(models.Model):

    anonym = models.BooleanField(null=False, blank=False, default=False)
    username = models.CharField(max_length=21, null=False, unique=True)
    email = models.EmailField(max_length=42, null=False, unique=True)
    feedback = models.TextField(max_length=214, blank=False)


class Booking(models.Model):

    username = models.CharField(max_length=21, null=False, blank=False)
    meeting_topic = models.CharField(max_length=42, null=False, blank=False)
