# Generated by Django 3.2.18 on 2023-04-07 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_profile_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='featured_image',
        ),
    ]
