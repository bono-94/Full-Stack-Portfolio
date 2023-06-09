# Generated by Django 3.2.18 on 2023-06-26 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0104_auto_20230625_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='funding_payout_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='industry',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_location_city',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_location_continent',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_location_country',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_location_planet',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='product',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='products_provided',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='project_owner',
            field=models.CharField(max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='service',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='post',
            name='services_provided',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='target_groups',
            field=models.TextField(blank=True, max_length=315, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='target_markets',
            field=models.TextField(blank=True, max_length=315, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=42, unique=True),
        ),
    ]
