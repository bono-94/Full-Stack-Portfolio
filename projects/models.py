from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone
from django.core.validators import MaxValueValidator
from datetime import date, datetime

STATUS = ((0, "Draft"), (1, "Published"))


class Profile(models.Model):

    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    slug = models.SlugField(max_length=210, unique=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, max_length=84)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    profile_color = models.CharField(max_length=7, default='#ffd041', blank=True, null=True)
    active_days = models.CharField(max_length=63, blank=True, null=True)
    active_hours = models.CharField(max_length=42, blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='offline',
        blank=True,
        null=True
    )

    verified = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    privacy = models.BooleanField(default=False)
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

    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    public_email = models.EmailField(max_length=42, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=21, blank=True, null=True)
    last_name = models.CharField(max_length=21, blank=True, null=True)
    location = models.CharField(max_length=21, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height_cm = models.IntegerField(validators=[MaxValueValidator(300)], null=True, blank=True)
    weight_kg = models.IntegerField(validators=[MaxValueValidator(500)], null=True, blank=True)

    industry = models.CharField(max_length=21, blank=False, null=True)
    company = models.CharField(max_length=42, blank=True, null=True)
    department = models.CharField(max_length=21, blank=False, null=True)
    occupation = models.CharField(max_length=42, blank=True, null=True)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    hours_per_week = models.PositiveIntegerField(null=True, blank=True)

    cv = models.FileField(upload_to='cv/', blank=True, null=True, max_length=84)
    education = models.CharField(max_length=210, blank=False, null=True)
    work_history = models.TextField(max_length=2100, blank=False, null=True)
    projects_portfolio = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Portfolio URL'
    )
    references = models.TextField(max_length=210, blank=False, null=True)
    recommendations = models.TextField(max_length=210, blank=False, null=True)

    projects_completed = models.TextField(max_length=210, blank=False, null=True)
    goals_completed = models.TextField(max_length=210, blank=False, null=True)
    missions_completed = models.TextField(max_length=210, blank=False, null=True)
    milestones_completed = models.TextField(max_length=210, blank=False, null=True)
    tasks_completed = models.TextField(max_length=210, blank=False, null=True)
    contribution = models.TextField(max_length=210, blank=False, null=True)

    knowledge = models.TextField(max_length=210, blank=False, null=True)
    languages = models.TextField(max_length=84, blank=False, null=True)
    skills = models.TextField(max_length=210, blank=False, null=True)
    strengths = models.TextField(max_length=210, blank=False, null=True)
    weaknesses = models.TextField(max_length=210, blank=False, null=True)

    focus_innovation = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_financials = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_planning = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_monitoring = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_quality = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_quantity = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_collaboration = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    focus_leadership = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)

    special_ops = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_finance = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_marketing = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_supply_chain = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_hr = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_tech = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_sustainability = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    special_research = models.IntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)

    certificates = models.TextField(max_length=210, blank=False, null=True)
    honors = models.TextField(max_length=210, blank=False, null=True)
    articles = models.TextField(max_length=210, blank=False, null=True)
    results = models.TextField(max_length=210, blank=False, null=True)
    awards = models.TextField(max_length=210, blank=False, null=True)
    recognition = models.TextField(max_length=210, blank=False, null=True)
    bigger_fish_results = models.FileField(upload_to='bigger_fish_results/', blank=True, null=True, max_length=84)

    business_rewards = models.TextField(max_length=210, blank=False, null=True)
    innovation_land_rewards = models.TextField(max_length=210, blank=False, null=True)

    summary = models.TextField(max_length=84, blank=False, null=True)
    bio = models.TextField(max_length=2100, blank=False, null=True)
    goals = models.TextField(max_length=210, blank=False, null=True)
    story = models.TextField(max_length=210, blank=False, null=True)
    journey = models.TextField(max_length=210, blank=False, null=True)
    future = models.TextField(max_length=210, blank=False, null=True)
    legacy = models.TextField(max_length=210, blank=False, null=True)
    change = models.TextField(max_length=210, blank=False, null=True)
    ideal_life = models.TextField(max_length=2100, blank=False, null=True)
    motivation_wall = models.TextField(max_length=2100, blank=False, null=True)
    interests_hobbies_wall = models.TextField(max_length=2100, blank=False, null=True)
    daily_routine = models.FileField(upload_to='daily_routine/', blank=True, null=True, max_length=84)

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
