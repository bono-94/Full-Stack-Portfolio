# Generated by Django 3.2.18 on 2023-04-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20230406_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
