# Generated by Django 3.2.18 on 2023-04-06 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='project_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
