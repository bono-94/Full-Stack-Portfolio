# Generated by Django 3.2.18 on 2023-03-22 22:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_rename_excerpt_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='anonym',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='private',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='content_note',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='note',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='user_image'),
        ),
    ]