from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime
from django.core.validators import FileExtensionValidator
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

STATUS = ((0, "Draft"), (1, "Published"))


# PROFILE MODEL
class Profile(models.Model):

    # CHOICES
    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    # PROFILE CARD
    slug = models.SlugField(max_length=210, unique=True, null=True)
    privacy = models.BooleanField(default=False)
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        max_length=84
    )
    profile_color = models.CharField(
        max_length=7,
        default='#ffd041',
        blank=True,
        null=True
        )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='offline',
        blank=True,
        null=True
    )
    profile_quote = models.CharField(max_length=84, blank=True, null=True)
    active_days = models.CharField(max_length=63, blank=True, null=True)
    active_hours = models.CharField(max_length=42, blank=True, null=True)
    verified = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    lifecoin_balance = models.IntegerField(null=True, blank=True)
    website_link = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Website URL'
    )
    facebook_link = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Facebook URL'
    )
    twitter_link = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Twitter URL'
    )
    instagram_link = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Instagram URL'
    )
    linkedin_link = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='LinkedIn URL'
    )
    youtube_link = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='YouTube URL'
    )
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    # USER VIDEO
    user_video = models.FileField(
        upload_to='user-videos/',
        blank=True,
        null=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[validate_video]
    )

    # GENERAL INFORMATION
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    public_email = models.EmailField(max_length=42, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=21, blank=True, null=True)
    last_name = models.CharField(max_length=21, blank=True, null=True)
    location = models.CharField(max_length=21, blank=True, null=True)
    languages = models.TextField(max_length=84, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height_cm = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)], null=True, blank=True)
    weight_kg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)], null=True, blank=True)

    # CURRENT EMPLOYMENT
    industry = models.CharField(max_length=21, blank=True, null=True)
    company = models.CharField(max_length=42, blank=True, null=True)
    department = models.CharField(max_length=21, blank=True, null=True)
    occupation = models.CharField(max_length=42, blank=True, null=True)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    hours_per_week = models.PositiveIntegerField(null=True, blank=True)

    # PREVIOUS EMPLOYMENT
    cv = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip'])],
        storage=RawMediaCloudinaryStorage(),
        )
    education = models.CharField(max_length=210, blank=True, null=True)
    work_history = models.TextField(max_length=2100, blank=True, null=True)
    projects_portfolio = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Portfolio URL'
    )
    references = models.TextField(max_length=210, blank=True, null=True)
    recommendations = models.TextField(max_length=210, blank=True, null=True)

    # ACHIEVEMENTS
    projects_completed = models.TextField(max_length=210, blank=True, null=True)
    goals_completed = models.TextField(max_length=210, blank=True, null=True)
    missions_completed = models.TextField(max_length=210, blank=True, null=True)
    milestones_completed = models.TextField(max_length=210, blank=True, null=True)
    tasks_completed = models.TextField(max_length=210, blank=True, null=True)
    contribution = models.TextField(max_length=210, blank=True, null=True)

    # ATTRIBUTES
    knowledge = models.TextField(max_length=210, blank=True, null=True)
    skills = models.TextField(max_length=210, blank=True, null=True)
    strengths = models.TextField(max_length=210, blank=True, null=True)
    weaknesses = models.TextField(max_length=210, blank=True, null=True)

    # BUSINESS FOCUS
    focus_innovation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_financials = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_planning = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_monitoring = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_quality = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_collaboration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_leadership = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    # BUSINESS SPECIALTY
    special_ops = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_finance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_marketing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_supply_chain = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_hr = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_tech = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_sustainability = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_research = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    # ACCOMPLISHMENTS
    results = models.TextField(max_length=210, blank=True, null=True)
    certificates = models.TextField(max_length=210, blank=True, null=True)
    honors = models.TextField(max_length=210, blank=True, null=True)
    articles = models.TextField(max_length=210, blank=True, null=True)
    recognition = models.TextField(max_length=210, blank=True, null=True)
    bigger_fish_results = models.ImageField(upload_to='bigger_fish_results/', blank=True, null=True, max_length=84)

    # REWARDS
    awards = models.TextField(max_length=210, blank=True, null=True)
    business_rewards = models.TextField(max_length=210, blank=True, null=True)
    innovation_land_rewards = models.TextField(max_length=210, blank=True, null=True)

    # PERSONAL WALL
    summary = models.TextField(max_length=84, blank=True, null=True)
    story = models.TextField(max_length=2100, blank=True, null=True)
    journey = models.TextField(max_length=210, blank=True, null=True)
    future = models.TextField(max_length=210, blank=True, null=True)
    legacy = models.TextField(max_length=210, blank=True, null=True)
    change = models.TextField(max_length=210, blank=True, null=True)
    ideal_life = models.TextField(max_length=2100, blank=True, null=True)
    goals = models.TextField(max_length=210, blank=True, null=True)
    motivation_wall = models.TextField(max_length=2100, blank=True, null=True)
    interests_hobbies_wall = models.TextField(max_length=2100, blank=True, null=True)
    daily_routine = models.FileField(
        upload_to='daily_routine/',
        blank=True,
        null=True,
        max_length=84,
        storage=RawMediaCloudinaryStorage(),
        validators=[FileExtensionValidator(
            allowed_extensions=[
                'xlsx',
                'xls',
                'xlsm',
                'xlsb',
                'csv',
                'parquet'
            ])],
    )

    # NAMING & SAVING
    def __str__(self):
        return f"{self.username} profile"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    # DURATION SINCE FOR CREATED ON & UPDATED ON
    def user_duration_created(self):
        if self.created_on is not None:
            duration = (timezone.now() - self.created_on).days
            return duration
        else:
            return None

    def user_duration_updated(self):
        if self.updated_on is not None:
            duration = (timezone.now() - self.updated_on).days
            return duration
        else:
            return None

    # AGE CALCULATION BY BIRTHDATE
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    # EMPLOYMENT DURATION
    def employed_days(self):
        today = timezone.now().date()
        duration = today - self.start_date
        return duration.days

    def employed_months(self):
        today = timezone.now().date()
        duration = today - self.start_date
        total_months = duration.days // 30   # Assuming 30 days per month
        return total_months

    def employed_years(self):
        today = timezone.now().date()
        duration = today - self.start_date
        total_years = duration.days // 365  # Assuming 365 days per year
        return total_years

    # PROGRESS BAR 1 - STYLE
    @property
    def focus_innovation_style(self):
        return f"width: {self.focus_innovation}%"

    @property
    def focus_financials_style(self):
        return f"width: {self.focus_financials}%"

    @property
    def focus_planning_style(self):
        return f"width: {self.focus_planning}%"

    @property
    def focus_monitoring_style(self):
        return f"width: {self.focus_monitoring}%"

    @property
    def focus_quality_style(self):
        return f"width: {self.focus_quality}%"

    @property
    def focus_quantity_style(self):
        return f"width: {self.focus_quantity}%"

    @property
    def focus_collaboration_style(self):
        return f"width: {self.focus_collaboration}%"

    @property
    def focus_leadership_style(self):
        return f"width: {self.focus_leadership}%"

    # PROGRESS BAR 2 - STYLE
    @property
    def special_ops_style(self):
        return f"width: {self.special_ops}%"

    @property
    def special_finance_style(self):
        return f"width: {self.special_finance}%"

    @property
    def special_marketing_style(self):
        return f"width: {self.special_marketing}%"

    @property
    def special_supply_chain_style(self):
        return f"width: {self.special_supply_chain}%"

    @property
    def special_hr_style(self):
        return f"width: {self.special_hr}%"

    @property
    def special_tech_style(self):
        return f"width: {self.special_tech}%"

    @property
    def special_sustainability_style(self):
        return f"width: {self.special_sustainability}%"

    @property
    def special_research_style(self):
        return f"width: {self.special_research}%"


# AUTOMATIC PROFILE CREATOR FROM USER MODEL
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)
        try:
            instance.user_profile.save()
        except Exception as e:
            print('No profile related to User')

    print(create_or_update_user_profile)


class Post(models.Model):

    slug = models.SlugField(max_length=210, unique=True)
    title = models.CharField(max_length=210, blank=False, unique=True)
    industry = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=50, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)
    project_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
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
        ordering = ['-created_on_note']

    def __str__(self):
        return f"Note {self.content_note} by {self.name}"

    def number_of_notes(self):
        return self.content_note.count()


class Request(models.Model):

    name = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(max_length=42, blank=False)
    request = models.TextField(max_length=428, blank=False)
    created_on_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
