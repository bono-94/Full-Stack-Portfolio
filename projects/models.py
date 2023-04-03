from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# The advantage of having a separate Profile model, as you do, is that you can add additional fields
# to the 'User' without actually messing with the base User model (which can be a nightmare).
# So long as there's a OneToOne relationship between User and Profile (as there is) you can always get ANY
#  information from either of them via the related name or field itself (user_profile and username)

# I will say that because you've got certain views written already, you might meet errors along the way,
# so just be prepared to perhaps delete existing users that might be tripping your old logic up.


class Profile(models.Model):

    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    slug = models.SlugField(max_length=210, unique=True, null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=21, blank=True, null=True)
    last_name = models.CharField(max_length=21, blank=True, null=True)
    location = models.CharField(max_length=21, blank=True, null=True)
    company = models.CharField(max_length=21, blank=True, null=True)
    occupation = models.CharField(max_length=21, blank=True, null=True)
    email = models.EmailField(max_length=42, unique=True, blank=True, null=True)
    bio = models.TextField(max_length=214, blank=True, null=True)

    def __str__(self):
        return f"{self.username} profile"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print('Signal fired on creation of User')
    print('Created? ', created)
    if created:
        Profile.objects.create(username=instance)
        try:
            instance.user_profile.save()
            print('Do we have a profile created? ', instance.user_profile)
        except Exception as e:
            print('No profile related to User')

    print(create_or_update_user_profile)


class Post(models.Model):

    slug = models.SlugField(max_length=210, unique=True)
    title = models.CharField(max_length=210, unique=True)
    industry = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
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
