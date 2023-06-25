from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from datetime import date, datetime
from django.core.validators import FileExtensionValidator
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.core.exceptions import ValidationError

# PROJECTS VISIBILITY
STATUS = ((0, "Draft"), (1, "Published"))


# PROFILE MODEL
class Profile(models.Model):

    # CHOICES

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    TYPE_OF_USER = (
        ('Human', 'Human'),
        ('AI', 'AI'),
    )

    # MAXIMUM FILE NAME LENGTH
    def validate_file_name_length(value):
        if len(value.name) > 84:
            raise ValidationError("Filename must be under 84 characters.")

    # MAXIMUM FILE SIZE
    def max_file_size_ten(value):
        limit = 10 * 1024 * 1024

        if value.size > limit:
            raise ValidationError("Please upload a file under 10 MB.")

    def max_file_size_hundred(value):
        limit = 100 * 1024 * 1024

        if value.size > limit:
            raise ValidationError("Please upload a file under 100 MB.")

    # PROFILE CARD
    slug = models.SlugField(max_length=210, unique=True, null=True)
    privacy = models.BooleanField(default=False)
    profile_card_privacy = models.BooleanField(default=False)

    profile_audio = models.FileField(
        upload_to='profile_audio/',
        blank=True,
        null=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[
            validate_file_name_length,
            max_file_size_hundred
        ]
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )

    profile_color = models.CharField(
        max_length=7,
        default='#ffc107',
        blank=True,
        null=True
    )

    profile_quote = models.CharField(max_length=84, blank=True, null=True)
    active_days = models.CharField(max_length=63, blank=True, null=True)
    active_hours = models.CharField(max_length=42, blank=True, null=True)
    user_type = models.CharField(max_length=5, choices=TYPE_OF_USER, blank=True, null=True)
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
    user_video_privacy = models.BooleanField(default=False)

    user_video = models.FileField(
        upload_to='user-videos/',
        blank=True,
        null=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[
            validate_video,
            validate_file_name_length,
            max_file_size_hundred
        ],
    )

    # GENERAL INFORMATION
    general_info_privacy = models.BooleanField(default=False)

    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    public_email = models.EmailField(max_length=42, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=42, blank=True, null=True)
    last_name = models.CharField(max_length=42, blank=True, null=True)
    location = models.CharField(max_length=42, blank=True, null=True)
    languages = models.TextField(max_length=210, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height_cm = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)], null=True, blank=True)
    weight_kg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)], null=True, blank=True)

    # OCCUPATION
    current_employment_privacy = models.BooleanField(default=False)

    industry = models.CharField(max_length=42, blank=True, null=True)
    organization = models.CharField(max_length=42, blank=True, null=True)
    department = models.CharField(max_length=21, blank=True, null=True)
    occupation = models.CharField(max_length=42, blank=True, null=True)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    hours_per_week = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(168)], null=True, blank=True)

    # PREVIOUS EMPLOYMENT
    history_employment_privacy = models.BooleanField(default=False)

    cv = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    education = models.TextField(max_length=840, blank=True, null=True)
    work_history = models.TextField(max_length=2100, blank=True, null=True)

    projects_portfolio = models.FileField(
        upload_to='portfolios/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    references = models.TextField(max_length=420, blank=True, null=True)
    recommendations = models.TextField(max_length=420, blank=True, null=True)

    # ACHIEVEMENTS
    achievements_privacy = models.BooleanField(default=False)

    projects_completed = models.TextField(max_length=840, blank=True, null=True)
    goals_completed = models.TextField(max_length=840, blank=True, null=True)
    missions_completed = models.TextField(max_length=840, blank=True, null=True)
    milestones_completed = models.TextField(max_length=840, blank=True, null=True)
    tasks_completed = models.TextField(max_length=840, blank=True, null=True)
    contribution = models.TextField(max_length=840, blank=True, null=True)

    # ATTRIBUTES
    attributes_privacy = models.BooleanField(default=False)

    knowledge = models.TextField(max_length=840, blank=True, null=True)
    skills = models.TextField(max_length=840, blank=True, null=True)
    strengths = models.TextField(max_length=840, blank=True, null=True)
    weaknesses = models.TextField(max_length=840, blank=True, null=True)

    # BUSINESS FOCUS
    focus_privacy = models.BooleanField(default=False)

    focus_innovation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_financials = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_planning = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_monitoring = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_quality = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_collaboration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_leadership = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    # BUSINESS SPECIALTY
    specialty_privacy = models.BooleanField(default=False)

    special_ops = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_finance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_marketing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_supply_chain = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_hr = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_tech = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_sustainability = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    special_research = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    # ACCOMPLISHMENTS
    accomplishments_privacy = models.BooleanField(default=False)

    results = models.TextField(max_length=840, blank=True, null=True)
    certificates = models.TextField(max_length=840, blank=True, null=True)
    honors = models.TextField(max_length=840, blank=True, null=True)
    articles = models.TextField(max_length=840, blank=True, null=True)
    recognition = models.TextField(max_length=840, blank=True, null=True)

    bigger_fish_results = models.FileField(
        upload_to='bigger_fish_results/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    # REWARDS
    rewards_privacy = models.BooleanField(default=False)

    awards = models.TextField(max_length=840, blank=True, null=True)
    business_rewards = models.TextField(max_length=840, blank=True, null=True)
    innovation_land_rewards = models.TextField(max_length=840, blank=True, null=True)

    # PERSONAL WALL
    user_wall_privacy = models.BooleanField(default=False)

    summary = models.TextField(max_length=210, blank=True, null=True)
    story = models.TextField(max_length=2100, blank=True, null=True)
    journey = models.TextField(max_length=2100, blank=True, null=True)
    future = models.TextField(max_length=2100, blank=True, null=True)
    legacy = models.TextField(max_length=2100, blank=True, null=True)
    change = models.TextField(max_length=2100, blank=True, null=True)
    ideal_life = models.TextField(max_length=2100, blank=True, null=True)
    goals = models.TextField(max_length=2100, blank=True, null=True)
    motivation_wall = models.TextField(max_length=2100, blank=True, null=True)
    interests_hobbies_wall = models.TextField(max_length=2100, blank=True, null=True)

    daily_routine = models.FileField(
        upload_to='daily_routine/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'xlsx',
                'xls',
                'xlsm',
                'xlsb',
                'csv',
                'parquet'
            ]),
            validate_file_name_length,
            max_file_size_hundred
        ],
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

    AUTHOR_TYPE = (
        ('Human', 'Human'),
        ('A.I.', 'A.I.'),
    )

    TYPE_OF_POST = (
        ('Organization', 'Organization'),
        ('Project', 'Project'),
        ('Product', 'Product'),
        ('Service', 'Service'),
    )

    TYPE_OF_OWNERSHIP_PCT_OFFER = (
        ('Organization', 'Organization'),
        ('Project', 'Project'),
        ('Product', 'Product'),
        ('Service', 'Service'),
        ('Combination', 'Combination'),
    )

    TYPE_OF_END_SERVICE_OR_PRODUCT = (
        ('Product', 'Product'),
        ('Service', 'Service'),
        ('Both', 'Both'),
    )

    # MAXIMUM FILE NAME LENGTH
    def validate_file_name_length(value):
        if len(value.name) > 84:
            raise ValidationError("Filename must be under 84 characters.")

    # MAXIMUM FILE SIZE
    def max_file_size_ten(value):
        limit = 10 * 1024 * 1024

        if value.size > limit:
            raise ValidationError("Please upload a file under 10 MB.")

    def max_file_size_hundred(value):
        limit = 100 * 1024 * 1024

        if value.size > limit:
            raise ValidationError("Please upload a file under 100 MB.")

    # STOCK VALIDATION - if doesnt work, remove self and replace one below with instance.

    def validate_stock_proposal(value, self):
        stocks_proposal = value
        stocks_supply = self.stocks_quantity_total_supply

        if stocks_proposal and stocks_supply and stocks_proposal > stocks_supply:
            raise ValidationError("Stocks offering cannot be higher than stocks supply.")

    # END PRODUCT OR SERVICE VALIDATION - if doesnt work, remove self and replace one below with instance.

    def validate_end_ps_proposal(value, self):
        stocks_offering = value
        stocks_supply = self.stocks_supply

        if stocks_offering and stocks_supply and stocks_offering > stocks_supply:
            raise ValidationError("Stocks offering cannot be higher than stocks supply.")

    # POST LIST CARD CONTENT
    post_list_description = models.CharField(max_length=84, blank=False, null=True)

    post_list_image = models.ImageField(
        upload_to='post_list_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )

    # POST STRUCTURE
    slug = models.SlugField(max_length=21, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_verification = models.BooleanField(default=False)
    votes = models.ManyToManyField(User, related_name="projects_votes")
    views = models.IntegerField(default=0)
    public_privacy = models.BooleanField(default=False)

    post_background_audio = models.FileField(
        upload_to='post_audio/',
        blank=True,
        null=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[
            validate_file_name_length,
            max_file_size_hundred
        ]
    )

    # PAGE CONSTANT
    # POST DETAIL KEY INFORMATION
    post_logo_image = models.ImageField(
        upload_to='post_logo_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )

    title = models.CharField(max_length=21, blank=False, unique=True)
    caption = models.CharField(max_length=42, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    author_type = models.CharField(max_length=5, choices=AUTHOR_TYPE, blank=False)
    project_owner = models.CharField(max_length=21,  blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    # PAGE 1
    # POST LANDING MEDIA
    post_banner_image = models.ImageField(
        upload_to='post_banner_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )

    # POST DETAIL GENERAL INFORMATION
    post_type = models.CharField(max_length=12, choices=TYPE_OF_POST, blank=False)
    industry = models.CharField(max_length=21, blank=False)    
    organization = models.CharField(max_length=21, blank=True)
    project = models.CharField(max_length=21, blank=True)
    product = models.CharField(max_length=21, blank=True)
    service = models.CharField(max_length=21, blank=True)
    post_location_city = models.CharField(max_length=21, blank=False)
    post_location_country = models.CharField(max_length=21, blank=False)
    post_location_continent = models.CharField(max_length=21, blank=False)
    post_location_planet = models.CharField(max_length=21, blank=False)

    # INTRODUCTION
    introduction_privacy = models.BooleanField(default=False)

    introduction = models.TextField(max_length=420, blank=True)

    # POST PITCH VIDEO
    post_video_privacy = models.BooleanField(default=False)

    post_video = models.FileField(
        upload_to='posts-videos/',
        blank=True,
        null=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[
            validate_video,
            validate_file_name_length,
            max_file_size_hundred
        ],
    )

    # POST LAUNCH
    launch_date_privacy = models.BooleanField(default=False)

    launch_date = models.DateField(default=timezone.now, blank=True)
    same_start_launch_date = models.BooleanField(default=False)

    # PAGE 2
    # POST DETAILS O/P/P/S
    post_opps_details_privacy = models.BooleanField(default=False)

    pps_vision = models.TextField(max_length=168, blank=True, null=True)
    pps_goals = models.TextField(max_length=168, blank=True, null=True)
    pps_missions = models.TextField(max_length=168, blank=True, null=True)
    pps_planner = models.TextField(max_length=168, blank=True, null=True)

    team = models.TextField(max_length=525, blank=True, null=True)
    partners = models.TextField(max_length=525, blank=True, null=True)
    collaborators = models.TextField(max_length=525, blank=True, null=True)
    sponsors = models.TextField(max_length=525, blank=True, null=True)
    community = models.TextField(max_length=525, blank=True, null=True)
    stakeholders = models.TextField(max_length=525, blank=True, null=True)
    shareholders = models.TextField(max_length=525, blank=True, null=True)
    ecosystem_relationship = models.TextField(max_length=525, blank=True, null=True)

    resources_requiered = models.TextField(max_length=210, blank=True, null=True)
    target_markets = models.TextField(max_length=210, blank=True, null=True)
    target_groups = models.TextField(max_length=210, blank=True, null=True)
    values_provided = models.TextField(max_length=210, blank=True, null=True)
    differentiation = models.TextField(max_length=210, blank=True, null=True)
    sdg_goals = models.TextField(max_length=525, blank=True, null=True)
    legal_protection = models.TextField(max_length=525, blank=True, null=True)
    franchizing_licencing = models.TextField(max_length=525, blank=True, null=True)

    risks = models.TextField(max_length=168, blank=True, null=True)
    challenges = models.TextField(max_length=168, blank=True, null=True)
    change = models.TextField(max_length=168, blank=True, null=True)
    impact = models.TextField(max_length=168, blank=True, null=True)

    # PAGE 3
    # POST MORE ABOUT US
    post_about_privacy = models.BooleanField(default=False)

    organization_info = models.TextField(max_length=525, blank=True, null=True)
    products_provided = models.CharField(max_length=42, blank=True, null=True)
    services_provided = models.CharField(max_length=42, blank=True, null=True)
    organization_mission = models.TextField(max_length=42, blank=True, null=True)
    organization_vision = models.TextField(max_length=42, blank=True, null=True)
    organization_culture = models.TextField(max_length=525, blank=True, null=True)

    strengths = models.TextField(max_length=168, blank=True, null=True)
    weaknesses = models.TextField(max_length=168, blank=True, null=True)
    opportunities = models.TextField(max_length=168, blank=True, null=True)
    threats = models.TextField(max_length=168, blank=True, null=True)

    focus_privacy = models.BooleanField(default=False)

    focus_innovation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_financials = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_planning = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_monitoring = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_quality = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_collaboration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    focus_leadership = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    specialty_privacy = models.BooleanField(default=False)

    special_ops = models.TextField(max_length=210, blank=True, null=True)
    special_finance = models.TextField(max_length=210, blank=True, null=True)
    special_marketing = models.TextField(max_length=210, blank=True, null=True)
    special_supply_chain = models.TextField(max_length=210, blank=True, null=True)
    special_hr = models.TextField(max_length=210, blank=True, null=True)
    special_tech = models.TextField(max_length=210, blank=True, null=True)
    special_sustainability = models.TextField(max_length=210, blank=True, null=True)
    special_research = models.TextField(max_length=210, blank=True, null=True)

    specialty_privacy_two = models.BooleanField(default=False)

    special_ops_two = models.TextField(max_length=210, blank=True, null=True)
    special_finance_two = models.TextField(max_length=210, blank=True, null=True)
    special_marketing_two = models.TextField(max_length=210, blank=True, null=True)
    special_supply_chain_two = models.TextField(max_length=210, blank=True, null=True)
    special_hr_two = models.TextField(max_length=210, blank=True, null=True)
    special_tech_two = models.TextField(max_length=210, blank=True, null=True)
    special_sustainability_two = models.TextField(max_length=210, blank=True, null=True)
    special_research_two = models.TextField(max_length=210, blank=True, null=True)

    percentage_special_privacy = models.BooleanField(default=False)

    percentage_special_ops = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_ops_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_finance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_finance_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_marketing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_marketing_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_supply_chain = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_supply_chain_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_hr = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_hr_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_tech = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_tech_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_sustainability = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_sustainability_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    percentage_special_research = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    percentage_special_research_two = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)

    # PAGE 4 ARTICLES
    # POST BODY
    post_body_privacy = models.BooleanField(default=False)

    main_content = models.TextField(max_length=2100, blank=True, null=True)
    business_knowledge = models.TextField(max_length=2100, blank=True, null=True)
    story = models.TextField(max_length=2100, blank=True, null=True)
    journey = models.TextField(max_length=2100, blank=True, null=True)
    future = models.TextField(max_length=2100, blank=True, null=True)
    legacy = models.TextField(max_length=2100, blank=True, null=True)

    # PAGE 6
    # POST BRIDGE - BUSINESS LIBRARY
    post_bridge_privacy_library = models.BooleanField(default=False)

    organizational_structure = models.FileField(
        upload_to='organizational_structures/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    flowchart = models.FileField(
        upload_to='flowcharts/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    agenda = models.FileField(
        upload_to='agendas/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    tasklist = models.FileField(
        upload_to='tasklists/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    schedule = models.FileField(
        upload_to='schedules/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'xlsx',
                'xls',
                'xlsm',
                'xlsb',
                'csv',
                'parquet'
            ]),
            validate_file_name_length,
            max_file_size_hundred
        ],
    )

    financial_reports = models.FileField(
        upload_to='financial_reports/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'xlsx',
                'xls',
                'xlsm',
                'xlsb',
                'csv',
                'parquet'
            ]),
            validate_file_name_length,
            max_file_size_hundred
        ],
    )

    supply_chain_map = models.FileField(
        upload_to='supply_chain_maps/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    data_architecture_map = models.FileField(
        upload_to='data_architecture_maps/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    standard_operational_procedures = models.FileField(
        upload_to='standard_operational_procedures/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    marketing_strategy_map = models.FileField(
        upload_to='marketing_strategy_maps/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    hr_handbook = models.FileField(
        upload_to='hr_handbooks/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    sustainability_report = models.FileField(
        upload_to='sustainability_reports/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    research_and_development_agenda = models.FileField(
        upload_to='research_and_development_agenda/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )
    
    promotional_materials = models.FileField(
        upload_to='promotional_materials/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    certification = models.FileField(
        upload_to='certifications/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    articles = models.FileField(
        upload_to='articles/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    # POST BRIDGE - BUSINESS CABINET
    post_bridge_privacy_cabinet = models.BooleanField(default=False)

    business_plan = models.FileField(
        upload_to='business_plans/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    implementation_plan = models.FileField(
        upload_to='implementation_plans/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    pestle_report = models.FileField(
        upload_to='pestle_reports/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    internal_report = models.FileField(
        upload_to='internal_reports/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    capabilities = models.FileField(
        upload_to='capabilities/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    business_model_canvas = models.FileField(
        upload_to='business_model_canvases/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    contracts = models.FileField(
        upload_to='contracts/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    terms_conditions = models.FileField(
        upload_to='terms_conditions/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage(),
        validators=[
            FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip']),
            validate_file_name_length,
            max_file_size_ten
        ],
    )

    # PAGE 7
    # POST PROPOSALS & OFFERS
    post_proposal_model_privacy = models.BooleanField(default=False)

    # FUNDING TIMING
    funding_start_date = models.DateField(default=timezone.now, blank=True, null=True)
    funding_end_date = models.DateField(default=timezone.now, blank=True, null=True)
    funding_infinite_end_date = models.BooleanField(default=False)
    funding_payout_date = models.DateField(blank=True, null=True)

    # STOCKS PROPOSAL
    stocks_quantity_total_supply = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)], blank=True, null=True)

    stocks_quantity_proposal = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999), validate_stock_proposal], blank=True, null=True)
    stocks_proposal_note = models.CharField(max_length=84, blank=True, null=True)
    stocks_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # OWNERSHIP PERCENTAGE PER O.P.P.S TYPES PROPOSAL
    ownership_percentage_opps_type = models.CharField(max_length=12, choices=TYPE_OF_OWNERSHIP_PCT_OFFER, blank=True, null=True)

    ownership_percentage_opps_quantity_proposal = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    ownership_percentage_opps_proposal_note = models.CharField(max_length=84, blank=True, null=True)
    ownership_percentage_opps_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # END PRODUCT OR SERVICE PROPOSAL
    end_product_or_service_type = models.CharField(max_length=7, choices=TYPE_OF_END_SERVICE_OR_PRODUCT, blank=True, null=True)
    end_product_or_service_total_supply = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)], blank=True, null=True)
    
    end_product_or_service_quantity_proposal = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999), validate_end_ps_proposal], blank=True, null=True)
    end_product_or_service_merch_proposal = models.TextField(max_length=84, blank=True, null=True)
    end_product_or_service_membership_proposal = models.TextField(max_length=84, blank=True, null=True)
    end_product_or_service_proposal_note = models.CharField(max_length=84, blank=True, null=True)
    end_product_or_service_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # LIFETIME DISCOUNT PERCENTAGE PROPOSAL
    lifetime_discount_percentages_quantity_proposal = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    lifetime_discount_percentages_quality_proposal_note = models.CharField(max_length=84, blank=True, null=True)
    lifetime_discount_percentages_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # GUARANTEEED TEAM POSITION PROPOSAL
    team_guaranteed_position_title_proposal = models.CharField(max_length=21, blank=True, null=True)
    team_guaranteed_responsibilities_proposal = models.TextField(max_length=84, blank=True, null=True)
    team_guaranteed_employment_conditions_proposal = models.TextField(max_length=84, blank=True, null=True)
    team_guaranteed_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # PARTNERSHIP PROPOSAL
    partnership_proposal = models.TextField(max_length=210, blank=True, null=True)
    partnership_proposal_return = models.TextField(max_length=210, blank=True, null=True)
    
    # COLLABORATION PROPOSAL
    collaboration_proposal = models.TextField(max_length=210, blank=True, null=True)
    collaboration_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # SPONSORSHIP PROPOSAL
    sponsorship_proposal = models.TextField(max_length=210, blank=True, null=True)
    sponsorship_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # OPEN PROPOSAL
    open_proposal = models.TextField(max_length=210, blank=True, null=True)
    open_proposal_proposal_return = models.TextField(max_length=210, blank=True, null=True)

    # PROPOSAL TERMS
    proposal_terms_and_conditions = models.TextField(max_length=1050, blank=True, null=True)

    # PAGE 8
    # POST PROPOSAL CONTACT
    post_contact_privacy = models.BooleanField(default=False)

    public_email = models.EmailField(max_length=42, blank=True, null=True)
    public_phone = models.CharField(max_length=21, blank=True, null=True)
    contact_days = models.TextField(max_length=63, blank=True, null=True)
    contact_hours = models.TextField(max_length=42, blank=True, null=True)

    website_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='Website URL'
    )

    facebook_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='Facebook URL'
    )

    twitter_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='Twitter URL'
    )
    
    instagram_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='Instagram URL'
    )

    linkedin_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='LinkedIn URL'
    )

    youtube_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='YouTube URL'
    )

    # ORDERING
    class Meta:
        ordering = ['-created_on']

    # NAMING & SAVING
    def __str__(self):
        return self.title

    original_title = None

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.original_title:
            self.slug = slugify(self.title)
        if not self.original_title:
            self.original_title = self.title
        return super().save(*args, **kwargs)

    # COUNTING PUBLIC OPINIONS
    def number_of_votes(self):
        return self.votes.count()

    # DURATION SINCE FOR CREATED ON & UPDATED ON
    def post_duration_created(self):
        if self.created_on is not None:
            duration = (timezone.now() - self.created_on).days
            return duration
        else:
            return None

    def post_duration_updated(self):
        if self.updated_on is not None:
            duration = (timezone.now() - self.updated_on).days
            return duration
        else:
            return None

    # POST LAUNCH DATE DURATION
    def post_launch_days(self):
        duration = (self.launch_date - date.today()).days
        return duration

    def post_launch_months(self):
        duration = (self.launch_date - date.today()).days
        total_months = duration // 30  # Assuming 30 days per month
        return total_months

    def post_launch_years(self):
        duration = (self.launch_date - date.today()).days
        total_years = duration // 365  # Assuming 365 days per year
        return total_years
    
    # POST OFFER DURATION
    def post_duration_days(self):
        duration = self.end_date - self.start_date
        return duration.days

    def post_duration_months(self):
        duration = self.end_date - self.start_date
        total_months = duration.days // 30   # Assuming 30 days per month
        return total_months

    def post_duration_years(self):
        duration = self.end_date - self.start_date
        total_years = duration.days // 365  # Assuming 365 days per year
        return total_years

    # POST PAYOUT DATE DURATION
    def post_payout_duration_days(self):
        today = date.today()
        duration = today - self.payout_date
        return duration.days

    def post_payout_duration_months(self):
        today = date.today()
        duration = today - self.payout_date
        total_months = duration.days // 30   # Assuming 30 days per month
        return total_months

    def post_payout_duration_years(self):
        today = date.today()
        duration = today - self.payout_date
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

# POST PAGE 11
class Note(models.Model):

    NOTE_CHOICES = (
        ('Comment', 'Comment'),
        ('Offer', 'Offer'),
        ('Feedback', 'Feedback'),
        ('Compliment', 'Compliment'),
        ('Critique', 'Critique'),
        ('Advice', 'Advice'),
        ('Features Request', 'Features Request'),
        ('Collaboration Request', 'Collaboration Request'),
        ('Partnership Request', 'Partnership Request'),
        ('Sponsorship Request', 'Sponsorship Request'),
        ('Fresh Ideas', 'Fresh Ideas'),
        ('Community Access', 'Community Access'),
        ('End-user Request', 'End-user Request'),
        ('Stakeholder Request', 'Stakeholder Request'),
        ('Other', 'Other'),
    )

    note_privacy = models.BooleanField(default=False)
    
    note = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='note')
    name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_note")
    email = models.EmailField(max_length=100, blank=True)
    content_note = models.TextField(max_length=500)
    created_on_note = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on_note']

    def __str__(self):
        return f"Note {self.content_note} by {self.name}"

    def number_of_notes(self):
        return self.content_note.count()

# CONTACT REQUEST
class Request(models.Model):

    name = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(max_length=42, blank=False)
    request = models.TextField(max_length=428, blank=False)
    created_on_request = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
