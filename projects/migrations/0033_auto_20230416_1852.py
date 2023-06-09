# Generated by Django 3.2.18 on 2023-04-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_rename_email_profile_public_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_quote',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='story',
            field=models.TextField(max_length=2100, null=True),
        ),
    ]
