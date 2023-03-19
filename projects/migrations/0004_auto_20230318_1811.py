# Generated by Django 3.2.18 on 2023-03-18 18:11

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20230313_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=21, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('password_two', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='username',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='user_note', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='note',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='industry',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=210, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=210, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=21, unique=True)),
                ('profile_title', models.CharField(max_length=42, unique=True)),
                ('user_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('private', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=21)),
                ('last_name', models.CharField(max_length=21)),
                ('location', models.CharField(max_length=21)),
                ('company', models.CharField(max_length=21)),
                ('occupation', models.CharField(max_length=21)),
                ('email', models.EmailField(max_length=42, unique=True)),
                ('bio', models.TextField(max_length=214)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonym', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=42, unique=True)),
                ('feedback', models.TextField(max_length=214)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_topic', models.CharField(max_length=42)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]