# Generated by Django 3.2.18 on 2023-07-08 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0116_auto_20230708_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='privacy',
            new_name='global_privacy',
        ),
    ]
