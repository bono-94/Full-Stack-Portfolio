# Generated by Django 3.2.18 on 2023-06-21 10:44

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0086_auto_20230621_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_author_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_author_images/', validators=[projects.models.Post.validate_file_name_length, projects.models.Post.max_file_size_ten]),
        ),
    ]