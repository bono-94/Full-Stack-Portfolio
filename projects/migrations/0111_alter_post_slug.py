# Generated by Django 3.2.18 on 2023-06-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0110_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=42, unique=True),
        ),
    ]