# Generated by Django 3.2.18 on 2023-04-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_profile_profile_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
