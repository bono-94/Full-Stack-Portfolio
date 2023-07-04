# Generated by Django 3.2.18 on 2023-07-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0111_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='email',
        ),
        migrations.RemoveField(
            model_name='note',
            name='name',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note_privacy',
        ),
        migrations.RemoveField(
            model_name='post',
            name='main_content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='story',
        ),
        migrations.AlterField(
            model_name='note',
            name='content_note',
            field=models.TextField(max_length=630),
        ),
        migrations.AlterField(
            model_name='post',
            name='launch_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]