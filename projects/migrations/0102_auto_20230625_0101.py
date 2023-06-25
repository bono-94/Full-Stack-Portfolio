# Generated by Django 3.2.18 on 2023-06-25 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0101_auto_20230625_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_color_primary',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_color_secondary',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_color_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_colors_list',
        ),
        migrations.AlterField(
            model_name='post',
            name='collaboration_proposal',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='collaboration_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='collaborators',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='community',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ecosystem_relationship',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_product_or_service_proposal_note',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_product_or_service_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='franchizing_licencing',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='legal_protection',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='lifetime_discount_percentages_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='lifetime_discount_percentages_quality_proposal_note',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='open_proposal',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='open_proposal_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization_culture',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization_info',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ownership_percentage_opps_proposal_note',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ownership_percentage_opps_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='partners',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='partnership_proposal',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='partnership_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='proposal_terms_and_conditions',
            field=models.TextField(blank=True, max_length=1050, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sdg_goals',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='shareholders',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_finance',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_finance_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_hr',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_hr_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_marketing',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_marketing_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_ops',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_ops_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_research',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_research_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_supply_chain',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_supply_chain_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_sustainability',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_sustainability_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_tech',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='special_tech_two',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sponsors',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sponsorship_proposal',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sponsorship_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='stakeholders',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='stocks_proposal_note',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='stocks_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='team',
            field=models.TextField(blank=True, max_length=525, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='team_guaranteed_employment_conditions_proposal',
            field=models.TextField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='team_guaranteed_proposal_return',
            field=models.TextField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='team_guaranteed_responsibilities_proposal',
            field=models.TextField(blank=True, max_length=84, null=True),
        ),
    ]
