# Generated by Django 3.2.18 on 2023-06-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0103_auto_20230625_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='organization_mission',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization_vision',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
    ]
