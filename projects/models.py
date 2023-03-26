from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Register(models.Model):

    username = models.CharField(max_length=21, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    password_two = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.username


class Profile(models.Model):

    profile_title = models.CharField(max_length=42, unique=True)
    user_image = CloudinaryField('user_image', default='placeholder')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=21, blank=False)
    last_name = models.CharField(max_length=21, blank=False)
    location = models.CharField(max_length=21, blank=False)
    company = models.CharField(max_length=21, blank=False)
    occupation = models.CharField(max_length=21, blank=False)
    email = models.EmailField(max_length=42, unique=True)
    bio = models.TextField(max_length=214)

    def __str__(self):
        return f"{self.username} profile"


class Post(models.Model):

    title = models.CharField(max_length=210, unique=True)
    industry = models.CharField(max_length=50)
    company = models.CharField(max_length=50, default='Independent')
    slug = models.SlugField(max_length=210, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=105, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    votes = models.ManyToManyField(User, related_name="projects_votes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_votes(self):
        return self.votes.count()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Note(models.Model):

    note = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='note')
    name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_note")
    email = models.EmailField(max_length=100, blank=True)
    content_note = models.TextField(max_length=500)
    created_on_note = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on_note']

    def __str__(self):
        return f"Note {self.content_note} by {self.name}"


class Feedback(models.Model):

    name = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(max_length=42, unique=True)
    feedback = models.TextField(max_length=214, blank=False)

    def __str__(self):
        return self.name
