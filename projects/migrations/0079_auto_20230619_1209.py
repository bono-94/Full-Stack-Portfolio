# Generated by Django 3.2.18 on 2023-06-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0078_auto_20230619_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
