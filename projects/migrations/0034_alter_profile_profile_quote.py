# Generated by Django 3.2.18 on 2023-04-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0033_auto_20230416_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_quote',
            field=models.CharField(blank=True, default='(blank)', max_length=84, null=True),
        ),
    ]
