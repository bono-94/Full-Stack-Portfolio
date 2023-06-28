# Generated by Django 3.2.18 on 2023-06-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0108_auto_20230628_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='proposal_fee_type',
            field=models.CharField(blank=True, choices=[('One-time Fee', 'One-time Fee'), ('Commision', 'Commision')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_product_or_service_proposal_costs',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='lifetime_discount_percentages_quality_proposal_costs',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ownership_percentage_opps_proposal_costs',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='stocks_proposal_costs',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='team_guaranteed_position_title_proposal',
            field=models.TextField(blank=True, max_length=42, null=True),
        ),
    ]
