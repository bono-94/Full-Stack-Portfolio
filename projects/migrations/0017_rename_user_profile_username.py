# Generated by Django 3.2.18 on 2023-04-03 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_rename_username_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
