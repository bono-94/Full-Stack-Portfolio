# Generated by Django 3.2.18 on 2023-06-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0081_auto_20230619_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_color_text',
            field=models.CharField(blank=True, default='#000000', max_length=7, null=True),
        ),
    ]
