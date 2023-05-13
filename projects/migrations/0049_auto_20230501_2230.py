# Generated by Django 3.2.18 on 2023-05-01 22:30

import cloudinary_storage.storage
import cloudinary_storage.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0048_alter_profile_projects_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_audio',
            field=models.FileField(blank=True, null=True, upload_to='profile_audio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bigger_fish_results',
            field=models.ImageField(blank=True, null=True, upload_to='bigger_fish_results/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects_portfolio',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='portfolios/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'zip'])]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_video',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='user-videos/', validators=[cloudinary_storage.validators.validate_video, django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])]),
        ),
    ]