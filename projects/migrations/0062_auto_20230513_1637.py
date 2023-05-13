# Generated by Django 3.2.18 on 2023-05-13 16:37

import django.core.validators
from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bigger_fish_results_extension',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bigger_fish_results',
            field=models.FileField(blank=True, null=True, upload_to='bigger_fish_results/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), projects.models.Profile.validate_file_name_length, projects.models.Profile.max_file_size_ten]),
        ),
    ]