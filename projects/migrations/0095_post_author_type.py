# Generated by Django 3.2.18 on 2023-06-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0094_auto_20230621_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_type',
            field=models.CharField(choices=[('Human', 'Human'), ('A.I.', 'A.I.')], max_length=5, null=True),
        ),
    ]
