# Generated by Django 3.2.18 on 2023-03-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='company',
            field=models.CharField(default='Independent', max_length=50),
        ),
    ]
