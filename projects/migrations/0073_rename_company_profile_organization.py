# Generated by Django 3.2.18 on 2023-06-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0072_auto_20230611_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='company',
            new_name='organization',
        ),
    ]