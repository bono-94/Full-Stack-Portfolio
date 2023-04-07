# Generated by Django 3.2.18 on 2023-04-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_feedback_created_on_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=42, unique=True)),
                ('request', models.TextField(max_length=428)),
                ('created_on_request', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
