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

    TYPE_OF_POST = (
        ('Organization', 'Organization'),
        ('Project', 'Project'),
        ('Product', 'Product'),
        ('Service', 'Service'),
    )

    TYPE_OF_FEE_MODEL = (
        ('One-time Fee', 'One-time Fee'),
        ('Percentage', 'Percentage'),
    )

    TYPE_OF_OFFER_MODEL = (
        ('Stocks', 'Stocks'),
        ('Ownership Percentage', 'Ownership Percentage'),
        ('Return Amount', 'Return Amount'),
        ('End Products/Services Quality', 'End Products/Services Quality'),
        ('End Products/Services Quantity', 'End Products/Services Quantity'),
        ('Lifetime Discount', 'Lifetime Discount'),
        ('Team Position', 'Team Position'),
        ('Partnership', 'Partnership'),
        ('Collaboration', 'Collaboration'),
        ('Sponsorship', 'Sponsorship'),
        ('Community Access', 'Community Access'),
        ('Pioneering', 'Pioneering'),
        ('Merchandize', 'Merchandize'),
        ('Special Acknowledgement', 'Special Acknowledgement'),
        ('Open Offers', 'Open Offers'),
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

    def validate_stock_offering(value, self):
        stocks_offering = value
        stocks_supply = self.stocks_supply

        if stocks_offering and stocks_supply and stocks_offering > stocks_supply:
            raise ValidationError("Stocks offering cannot be higher than stocks supply.")

    # POST LIST DESIGN
    post_list_description = models.CharField(max_length=84, blank=True, null=True)
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
    votes = models.ManyToManyField(User, related_name="projects_votes", blank=True)
    views = models.IntegerField(default=0, blank=True)
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
    post_colors_list = models.BooleanField(default=False)
    post_color_primary = models.CharField(
        max_length=7,
        default='#292b2c',
        blank=True,
        null=True
    )
    post_color_secondary = models.CharField(
        max_length=7,
        default='#ffc107',
        blank=True,
        null=True
    )
    post_color_text = models.CharField(
        max_length=7,
        default='#000000',
        blank=True,
        null=True
    )

    # POST INTRODUCTION
    post_logo_image = models.ImageField(
        upload_to='post_logo_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )
    post_banner_image = models.ImageField(
        upload_to='post_banner_images/',
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
    project_owner = models.CharField(max_length=21, blank=False)

    post_type = models.CharField(max_length=12, choices=TYPE_OF_POST, blank=False, null=True)
    industry = models.CharField(max_length=21, blank=False)    
    organization = models.CharField(max_length=21, blank=False)
    project = models.CharField(max_length=21, blank=False)
    product = models.CharField(max_length=21, blank=False)
    service = models.CharField(max_length=21, blank=False)

    post_location_city = models.CharField(max_length=21, blank=False, null=True)
    post_location_country = models.CharField(max_length=21, blank=False, null=True)
    post_location_continent = models.CharField(max_length=21, blank=False, null=True)
    post_location_planet = models.CharField(max_length=21, blank=False, null=True)

    launch_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(default=timezone.now, blank=True, null=True)
    infinite_end_date = models.BooleanField(default=False)

    introduction = models.TextField(max_length=210, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    #  POST PITCH VIDEO
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

    # POST ABOUT
    post_about_privacy = models.BooleanField(default=False)

    organization_info = models.TextField(max_length=210, blank=True, null=True)
    organization_culture = models.TextField(max_length=210, blank=True, null=True)
    organization_mission = models.CharField(max_length=42, blank=True, null=True)
    organization_vision = models.CharField(max_length=42, blank=True, null=True)

    products_provided = models.CharField(max_length=42, blank=True, null=True)
    services_provided = models.CharField(max_length=42, blank=True, null=True)

    pps_objectives = models.TextField(max_length=210, blank=True, null=True)
    pps_goals = models.TextField(max_length=210, blank=True, null=True)
    pps_milestones = models.TextField(max_length=210, blank=True, null=True)

    team = models.TextField(max_length=210, blank=True, null=True)
    partners = models.TextField(max_length=210, blank=True, null=True)
    collaborators = models.TextField(max_length=210, blank=True, null=True)
    sponsors = models.TextField(max_length=210, blank=True, null=True)
    community = models.TextField(max_length=210, blank=True, null=True)
    stakeholders = models.TextField(max_length=210, blank=True, null=True)
    shareholders = models.TextField(max_length=210, blank=True, null=True)

    resources_requiered = models.TextField(max_length=210, blank=True, null=True)
    target_markets = models.TextField(max_length=210, blank=True, null=True)
    target_group = models.TextField(max_length=210, blank=True, null=True)
    values_provided = models.TextField(max_length=210, blank=True, null=True)
    differentiation = models.TextField(max_length=210, blank=True, null=True)
    sdg_goals = models.TextField(max_length=210, blank=True, null=True)
    intellectual_property = models.TextField(max_length=210, blank=True, null=True)
    legal_protection = models.TextField(max_length=210, blank=True, null=True)
    licencing = models.TextField(max_length=210, blank=True, null=True)
    franchizing = models.TextField(max_length=210, blank=True, null=True)

    risks = models.TextField(max_length=210, blank=True, null=True)
    challenges = models.TextField(max_length=210, blank=True, null=True)
    change = models.TextField(max_length=210, blank=True, null=True)
    impact = models.TextField(max_length=210, blank=True, null=True)

    strengths = models.TextField(max_length=210, blank=True, null=True)
    weaknesses = models.TextField(max_length=210, blank=True, null=True)
    opportunities = models.TextField(max_length=210, blank=True, null=True)
    threats = models.TextField(max_length=210, blank=True, null=True)

    focus_privacy = models.BooleanField(default=False)
    focus_innovation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_financials = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_planning = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_monitoring = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_quality = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_collaboration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    focus_leadership = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

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

    # POST BODY
    post_body_privacy = models.BooleanField(default=False)

    main_content = models.TextField(max_length=8400, blank=True, null=True)
    business_knowledge = models.TextField(max_length=8400, blank=True, null=True)

    story = models.TextField(max_length=2100, blank=True, null=True)
    journey = models.TextField(max_length=2100, blank=True, null=True)
    future = models.TextField(max_length=2100, blank=True, null=True)
    legacy = models.TextField(max_length=2100, blank=True, null=True)

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
    timeline = models.FileField(
        upload_to='timelines/',
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

    # POST BRIDGE - BUSINESS DOCUMENTS
    post_bridge_privacy_documents = models.BooleanField(default=False)
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

    # POST CONCLUSION
    post_conclusion_privacy = models.BooleanField(default=False)
    post_fee_model_privacy = models.BooleanField(default=False)

    fee_model = models.CharField(max_length=12, choices=TYPE_OF_FEE_MODEL, blank=True, null=True)
    offer_model = models.CharField(max_length=30, choices=TYPE_OF_OFFER_MODEL, blank=True, null=True)

    amount_requested = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)], null=True, blank=True)
    payout_date = models.DateField(blank=True, null=True)

    stocks_offering = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999), validate_stock_offering], null=True, blank=True)
    stocks_supply = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)], null=True, blank=True)
    ownership_percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    return_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)], null=True, blank=True)
    end_product_or_service_quality = models.TextField(max_length=210, blank=True, null=True)
    end_product_or_service_quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)], null=True, blank=True)
    lifetime_discount_percentages = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    team_guaranteed_position = models.CharField(max_length=42, blank=True, null=True)
    partnership = models.TextField(max_length=210, blank=True, null=True)
    collaboration = models.TextField(max_length=210, blank=True, null=True)
    sponsorship = models.TextField(max_length=210, blank=True, null=True)
    community_access = models.BooleanField(default=False)
    pioneering = models.BooleanField(default=False)
    merchandize = models.TextField(max_length=210, blank=True, null=True)
    special_acknowledgement = models.TextField(max_length=210, blank=True, null=True)
    open_offers = models.BooleanField(default=False)

    offer_terms = models.TextField(max_length=8400, blank=True, null=True)

    # POST CONTACT
    post_contact_privacy = models.BooleanField(default=False)
    post_public_email = models.EmailField(max_length=42, blank=True, null=True)
    public_phone = models.CharField(max_length=21, blank=True, null=True)
    contact_days = models.CharField(max_length=63, blank=True, null=True)
    contact_hours = models.CharField(max_length=42, blank=True, null=True)
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

    # POST EVENT
    event_privacy = models.BooleanField(default=False)
    event_color = models.CharField(
        max_length=7,
        default='#ffc107',
        blank=True,
        null=True
    )
    event_image = models.ImageField(
        upload_to='post_event_images/',
        blank=True,
        null=True,
        validators=[
            validate_file_name_length,
            max_file_size_ten
        ]
    )
    event_link = models.URLField(
        max_length=210,
        blank=True,
        null=True,
        verbose_name='Event URL'
    )
    event_title = models.CharField(max_length=84, blank=True, null=True)
    event_host = models.CharField(max_length=42, blank=True, null=True)
    event_content = models.TextField(max_length=420, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_hour = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], null=True, blank=True)
    event_minute = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)], null=True, blank=True)
    event_location = models.CharField(max_length=42, blank=True, null=True)
    event_price = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999)], null=True, blank=True)
    event_price_cents = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True, blank=True)
    event_capacity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)], null=True, blank=True)

    rspv_yes = models.ManyToManyField(User, related_name="rspv_yes", blank=True)
    rspv_no = models.ManyToManyField(User, related_name="rspv_no", blank=True)
    rspv_maybe = models.ManyToManyField(User, related_name="rspv_maybe", blank=True)
    rspv_next_time = models.ManyToManyField(User, related_name="rspv_next_time", blank=True)

    # POST RESULTS
    post_results_privacy = models.BooleanField(default=False)
    number_of_phases = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)], null=True, blank=True)

    amount_asked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999999)], null=True, blank=True)
    amount_collected = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999999)], null=True, blank=True)

    ownership_offered = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    ownerhip_given = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    team_positions_offered = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21042004)], null=True, blank=True)
    team_positions_given = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21042004)], null=True, blank=True)

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

    # COUNTING OF EVENT RSPVS

    def number_of_rspv_yes(self):
        return self.rspv_yes.count()

    def number_of_rspv_no(self):
        return self.rspv_no.count()

    def number_of_rspv_maybe(self):
        return self.rspv_maybe.count()

    def number_of_rspv_next_time(self):
        return self.rspv_next_time.count()

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

    # POST PROJECTED DURATION
    def post_duration_days(self):
        duration = self.end_date - self.launch_date
        return duration.days

    def post_duration_months(self):
        duration = self.end_date - self.launch_date
        total_months = duration.days // 30   # Assuming 30 days per month
        return total_months

    def post_duration_years(self):
        duration = self.end_date - self.launch_date
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


class Request(models.Model):

    name = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(max_length=42, blank=False)
    request = models.TextField(max_length=428, blank=False)
    created_on_request = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
