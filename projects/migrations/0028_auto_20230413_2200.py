# Generated by Django 3.2.18 on 2023-04-13 22:00

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_alter_note_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active_days',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_hours',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='articles',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='awards',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bigger_fish_results',
            field=models.FileField(blank=True, max_length=84, null=True, upload_to='bigger_fish_results/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='business_rewards',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='certificates',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='change',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contribution',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, max_length=84, null=True, upload_to='cv/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='daily_routine',
            field=models.FileField(blank=True, max_length=84, null=True, upload_to='daily_routine/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_collaboration',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_financials',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_innovation',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_leadership',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_monitoring',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_planning',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_quality',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='focus_quantity',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='future',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='goals',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='goals_completed',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='height_cm',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='honors',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hours_per_week',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ideal_life',
            field=models.TextField(max_length=2100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='industry',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='innovation_land_rewards',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='Instagram URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests_hobbies_wall',
            field=models.TextField(max_length=2100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='journey',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='knowledge',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.TextField(max_length=84, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='legacy',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lifecoin_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='LinkedIn URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='milestones_completed',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='missions_completed',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='motivation_wall',
            field=models.TextField(max_length=2100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='privacy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects_completed',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects_portfolio',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='Portfolio URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='recognition',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='recommendations',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='references',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='results',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_finance',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_hr',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_marketing',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_ops',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_research',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_supply_chain',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_sustainability',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='special_tech',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('online', 'Online'), ('offline', 'Offline')], default='offline', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='story',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='strengths',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='summary',
            field=models.TextField(max_length=84, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tasks_completed',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='Twitter URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='weaknesses',
            field=models.TextField(max_length=210, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_link',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='Website URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight_kg',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_history',
            field=models.TextField(max_length=2100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_link',
            field=models.URLField(blank=True, max_length=210, null=True, unique=True, verbose_name='YouTube URL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=84, null=True, upload_to='profile_images/'),
        ),
    ]
