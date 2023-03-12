from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    industry = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    votes = models.ManyToManyField(User, related_name="projects_votes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_votes(self):
        return self.votes.count()


class Notes(models.Model):

    note = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content_notes = models.TextField()
    created_on_notes = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on_notes']

    def __str__(self):
        return f"Note {self.content_notes} by {self.name}"
