# Generated by Django 3.2.18 on 2023-03-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]