# Generated by Django 3.2.18 on 2023-07-08 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0113_auto_20230705_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='current_employment_privacy',
            new_name='occupation_privacy',
        ),
    ]
