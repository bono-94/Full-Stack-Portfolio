# Generated by Django 3.2.18 on 2023-07-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0123_alter_post_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='team_guaranteed_position_title_proposal',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
    ]
