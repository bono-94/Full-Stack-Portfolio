# Generated by Django 3.2.18 on 2023-06-21 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0091_alter_post_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_type',
        ),
    ]
