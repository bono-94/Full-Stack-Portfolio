"""
Creation and configuration of custom forms for the application.
These forms are used for creating and updating various models.
Each form provides fields and validation specific to the relevant model.
"""

from django import forms
from .models import Profile, Post, Note
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator


# PROFILE FORM
class ProfileForm(forms.ModelForm):
    """
    Form used for creating or updating a user profile.
    """
    class Meta:
        model = Profile
        fields = [
            # PUBLIC VISIBILITY
            'global_privacy',
            # PROFILE CARD
            'profile_card_privacy',
            'profile_color',
            'profile_audio',
            'profile_image',
            'profile_quote',
            'user_type',
            'active_days',
            'active_hours',
            'website_link',
            'facebook_link',
            'twitter_link',
            'instagram_link',
            'linkedin_link',
            'youtube_link',
            # USER VIDEO
            'user_video_privacy',
            'user_video',
            # GENERAL INFORMATION
            'general_info_privacy',
            'public_email',
            'first_name',
            'last_name',
            'location',
            'languages',
            'gender',
            'date_of_birth',
            'height_cm',
            'weight_kg',
            # OCCUPATION
            'occupation_privacy',
            'industry',
            'organization',
            'department',
            'occupation',
            'start_date',
            'hours_per_week',
            # CAREER
            'career_privacy',
            'cover_letter',
            'education',
            'work_history',
            'full_resume',
            'references',
            'recommendations',
            # ACHIEVEMENTS
            'achievements_privacy',
            'projects_completed',
            'goals_completed',
            'missions_completed',
            'milestones_completed',
            'tasks_completed',
            'contribution',
            # ATTRIBUTES
            'attributes_privacy',
            'knowledge',
            'skills',
            'strengths',
            'weaknesses',
            # BUSINESS FOCUS
            'focus_privacy',
            'focus_innovation',
            'focus_financials',
            'focus_planning',
            'focus_monitoring',
            'focus_quality',
            'focus_quantity',
            'focus_collaboration',
            'focus_leadership',
            # BUSINESS SPECIALTY
            'specialty_privacy',
            'special_ops',
            'special_finance',
            'special_marketing',
            'special_supply_chain',
            'special_hr',
            'special_tech',
            'special_sustainability',
            'special_research',
            # ACCOMPLISHMENTS
            'accomplishments_privacy',
            'results',
            'certificates',
            'honors',
            'articles',
            'recognition',
            'bigger_fish_results',
            # REWARDS
            'rewards_privacy',
            'awards',
            'business_rewards',
            'innovation_land_rewards',
            # PERSONAL WALL
            'user_wall_privacy',
            'summary',
            'story',
            'journey',
            'future',
            'legacy',
            'change',
            'ideal_life',
            'goals',
            'motivation_wall',
            'interests_hobbies_wall',
            'daily_routine',
        ]

        # CUSTOM INPUT TYPES
        widgets = {
            'profile_color': forms.TextInput(attrs={'type': 'color'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # FORM CLEANING AND VALIDATING
    def clean(self):
        """
        Validates the profile form data.
        Performs additional validation on the form data with emphasis on focus.
        If the sum of paired focus fields is equal to 100 is correct.
        Returns: cleaned form data.
        If sum is not integer 100, it raises an error to inform user.
        """

        cleaned_data = super().clean()
        focus_fields = [
            'focus_innovation',
            'focus_financials',
            'focus_planning',
            'focus_monitoring',
            'focus_quality',
            'focus_quantity',
            'focus_collaboration',
            'focus_leadership',
        ]

        focus_values = [cleaned_data.get(field) for field in focus_fields]
        for i in range(0, 8, 2):
            if not all(focus_values[i:i+2]):
                continue
            if sum(focus_values[i:i+2]) != 100:
                msg = f"The sum of {focus_fields[i].split('_', 1)[1]} and " \
                    f"{focus_fields[i+1].split('_', 1)[1]} must be equal " \
                    f"to 100."
                self.add_error(focus_fields[i], msg)
                self.add_error(focus_fields[i+1], msg)

        return cleaned_data


# POST FORM
class PostForm(forms.ModelForm):
    """
    Form used for creating or updating a user's posts.
    """

    # CUSTOM LABELLING AND VALIDATION
    pps_vision = forms.CharField(
        label='Post vision',
        required=False,
        validators=[MaxLengthValidator(168)]
    )

    pps_missions = forms.CharField(
        label='Post missions',
        required=False,
        validators=[MaxLengthValidator(168)]
    )

    pps_goals = forms.CharField(
        label='Post goals',
        required=False,
        validators=[MaxLengthValidator(168)]
    )

    pps_planner = forms.CharField(
        label='Post planner',
        required=False,
        validators=[MaxLengthValidator(168)]
    )

    sdg_goals = forms.CharField(
        label='SDG goals',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        validators=[MaxLengthValidator(525)]
    )

    special_ops = forms.CharField(
        label='Current Operations',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_ops_two = forms.CharField(
        label='Future Operations',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_ops = forms.IntegerField(
        label='Percentage Current Operations',
        required=False
    )

    percentage_special_ops_two = forms.IntegerField(
        label='Percentage Future Operations',
        required=False
    )

    special_supply_chain = forms.CharField(
        label='Current Supply Chain',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_supply_chain_two = forms.CharField(
        label='Future Supply Chain',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_supply_chain = forms.IntegerField(
        label='Percentage Current Supply Chain',
        required=False
    )

    percentage_special_supply_chain_two = forms.IntegerField(
        label='Percentage Future Supply Chain',
        required=False
    )

    special_tech = forms.CharField(
        label='Current Tech',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_tech_two = forms.CharField(
        label='Future Tech',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_tech = forms.IntegerField(
        label='Percentage Current Tech',
        required=False
    )

    percentage_special_tech_two = forms.IntegerField(
        label='Percentage Future Tech',
        required=False
    )

    special_hr = forms.CharField(
        label='Current HR',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_hr_two = forms.CharField(
        label='Future HR',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_hr = forms.IntegerField(
        label='Percentage Current HR',
        required=False
    )

    percentage_special_hr_two = forms.IntegerField(
        label='Percentage Future HR',
        required=False
    )

    special_finance = forms.CharField(
        label='Current Financial',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_finance_two = forms.CharField(
        label='Future Financial',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_finance = forms.IntegerField(
        label='Percentage Current Financial',
        required=False
    )

    percentage_special_finance_two = forms.IntegerField(
        label='Percentage Future Financial',
        required=False
    )

    special_marketing = forms.CharField(
        label='Current Marketing',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_marketing_two = forms.CharField(
        label='Future Marketing',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_marketing = forms.IntegerField(
        label='Percentage Current Marketing',
        required=False
    )

    percentage_special_marketing_two = forms.IntegerField(
        label='Percentage Future Marketing',
        required=False
    )

    special_research = forms.CharField(
        label='Current Research',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_research_two = forms.CharField(
        label='Future Research',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_research = forms.IntegerField(
        label='Percentage Current Research',
        required=False
    )

    percentage_special_research_two = forms.IntegerField(
        label='Percentage Future Research',
        required=False
    )

    special_sustainability = forms.CharField(
        label='Current Sustainability',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    special_sustainability_two = forms.CharField(
        label='Future Sustainability',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    percentage_special_sustainability = forms.IntegerField(
        label='Percentage Current Sustainability',
        required=False
    )

    percentage_special_sustainability_two = forms.IntegerField(
        label='Percentage Future Sustainability',
        required=False
    )

    ownership_percentage_opps_quantity_proposal = forms.FloatField(
        label='Ownership percentage proposal',
        required=False,
    )

    ownership_percentage_opps_proposal_return = forms.CharField(
        label='Ownership percentage return',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    ownership_percentage_opps_proposal_costs = forms.CharField(
        label='Ownership percentage costs',
        required=False,
        validators=[MaxLengthValidator(210)]
    )

    class Meta:
        model = Post
        fields = [
            # POST LIST CONTENT
            'post_list_description',
            'post_list_image',
            # POST STRUCTURE
            'public_privacy',
            'post_background_audio',
            'post_colors_list',
            'post_colors_details',
            'post_color_primary',
            'post_color_secondary',
            'post_color_text',
            # POST KEY INFORMATION
            'post_logo_image',
            'post_banner_image',
            'title',
            'caption',
            'author_type',
            'project_owner',
            # POST GENERAL INFORMATION
            'post_type',
            'industry',
            'organization',
            'project',
            'product',
            'service',
            'post_location_city',
            'post_location_country',
            'post_location_continent',
            'post_location_planet',
            # INTRODUCTION
            'introduction_privacy',
            'introduction',
            # POST VIDEO
            'post_video_privacy',
            'post_video',
            # POST LAUNCH
            'launch_date_privacy',
            'launch_date',
            # POST OPPS SPECIFICS
            'post_opps_details_privacy',
            'pps_vision',
            'pps_missions',
            'pps_goals',
            'pps_planner',
            'team',
            'partners',
            'collaborators',
            'sponsors',
            'community',
            'stakeholders',
            'shareholders',
            'ecosystem_relationship',
            'resources_requiered',
            'target_markets',
            'target_groups',
            'values_provided',
            'differentiation',
            'sdg_goals',
            'legal_protection',
            'franchizing_licencing',
            'risks',
            'challenges',
            'change',
            'impact',
            # POST ABOUT US SPECIFICS
            'post_about_privacy',
            'organization_info',
            'organization_mission',
            'organization_vision',
            'organization_culture',
            'products_provided',
            'services_provided',
            'strengths',
            'weaknesses',
            'opportunities',
            'threats',
            'focus_privacy',
            'focus_innovation',
            'focus_financials',
            'focus_planning',
            'focus_monitoring',
            'focus_quality',
            'focus_quantity',
            'focus_collaboration',
            'focus_leadership',
            'specialty_privacy',
            'specialty_privacy_two',
            'percentage_special_privacy',
            'special_ops',
            'special_ops_two',
            'percentage_special_ops',
            'percentage_special_ops_two',
            'special_supply_chain',
            'special_supply_chain_two',
            'percentage_special_supply_chain',
            'percentage_special_supply_chain_two',
            'special_tech',
            'special_tech_two',
            'percentage_special_tech',
            'percentage_special_tech_two',
            'special_hr',
            'special_hr_two',
            'percentage_special_hr',
            'percentage_special_hr_two',
            'special_finance',
            'special_finance_two',
            'percentage_special_finance',
            'percentage_special_finance_two',
            'special_marketing',
            'special_marketing_two',
            'percentage_special_marketing',
            'percentage_special_marketing_two',
            'special_research',
            'special_research_two',
            'percentage_special_research',
            'percentage_special_research_two',
            'special_sustainability',
            'special_sustainability_two',
            'percentage_special_sustainability',
            'percentage_special_sustainability_two',
            # POST BODY
            'post_body_privacy',
            'business_knowledge',
            'journey',
            'future',
            'legacy',
            # POST BRIDGE - BUSINESS LIBRARY
            'post_bridge_privacy_library',
            'organizational_structure',
            'flowchart',
            'agenda',
            'tasklist',
            'schedule',
            'financial_reports',
            'supply_chain_map',
            'data_architecture_map',
            'standard_operational_procedures',
            'marketing_strategy_map',
            'hr_handbook',
            'sustainability_report',
            'research_and_development_agenda',
            'promotional_materials',
            'certification',
            'articles',
            # POST BRIDGE - BUSINESS DOCUMENTS
            'post_bridge_privacy_cabinet',
            'business_plan',
            'implementation_plan',
            'pestle_report',
            'internal_report',
            'capabilities',
            'business_model_canvas',
            'contracts',
            'terms_conditions',
            # POST PROPOSALS & OFFERS
            'post_proposal_model_privacy',
            'proposal_fee_type',
            'same_start_launch_date',
            'funding_start_date',
            'funding_end_date',
            'funding_infinite_end_date',
            'funding_payout_date',
            'stocks_quantity_total_supply',
            'stocks_quantity_proposal',
            'stocks_proposal_return',
            'stocks_proposal_costs',
            'ownership_percentage_opps_type',
            'ownership_percentage_opps_quantity_proposal',
            'ownership_percentage_opps_proposal_return',
            'ownership_percentage_opps_proposal_costs',
            'end_product_or_service_type',
            'end_product_or_service_total_supply',
            'end_product_or_service_quantity_proposal',
            'end_product_or_service_proposal_return',
            'end_product_or_service_merch_proposal',
            'end_product_or_service_membership_proposal',
            'end_product_or_service_proposal_costs',
            'lifetime_discount_percentages_quantity_proposal',
            'lifetime_discount_percentages_proposal_return',
            'lifetime_discount_percentages_quality_proposal_costs',
            'team_guaranteed_position_title_proposal',
            'team_guaranteed_responsibilities_proposal',
            'team_guaranteed_employment_conditions_proposal',
            'team_guaranteed_proposal_costs',
            'partnership_proposal_return',
            'partnership_proposal_costs',
            'collaboration_proposal_return',
            'collaboration_proposal_costs',
            'sponsorship_proposal_return',
            'sponsorship_proposal_costs',
            'open_proposal_proposal_return',
            'open_proposal_costs',
            'proposal_terms_and_conditions',
            # POST PROPOSAL CONTACT
            'post_contact_privacy',
            'public_email',
            'public_phone',
            'contact_days',
            'contact_hours',
            'website_link',
            'facebook_link',
            'twitter_link',
            'instagram_link',
            'linkedin_link',
            'youtube_link',
        ]

        # CUSTOM INPUT TYPES
        widgets = {
            'post_color_primary': forms.TextInput(attrs={'type': 'color'}),
            'post_color_secondary': forms.TextInput(attrs={'type': 'color'}),
            'post_color_text': forms.TextInput(attrs={'type': 'color'}),
            'launch_date': forms.DateInput(attrs={'type': 'date'}),
            'funding_end_date': forms.DateInput(attrs={'type': 'date'}),
            'funding_start_date': forms.DateInput(attrs={'type': 'date'}),
            'funding_payout_date': forms.DateInput(attrs={'type': 'date'}),
            'payout_date': forms.DateInput(attrs={'type': 'date'}),
            'event_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        """
        Validates the profile form data.
        Performs additional validation on the form data with emphasis on focus.
        If the sum of paired focus fields is equal to 100 is correct.
        Returns cleaned form data.
        If sum is not integer 100, it raises an error to inform user.
        In addition it validates that 2 proposals are withing limitations.
        If quantity offer is larger than supply, it raises error.
        """

        cleaned_data = super().clean()
        focus_fields = [
            'focus_innovation',
            'focus_financials',
            'focus_planning',
            'focus_monitoring',
            'focus_quality',
            'focus_quantity',
            'focus_collaboration',
            'focus_leadership',
        ]

        total_supply = cleaned_data.get('stocks_quantity_total_supply')
        proposal = cleaned_data.get('stocks_quantity_proposal')
        pos_supply = cleaned_data.get('end_product_or_service_total_supply')
        pos_proposal = cleaned_data.get(
            'end_product_or_service_quantity_proposal'
            )

        focus_values = [cleaned_data.get(field) for field in focus_fields]
        for i in range(0, 8, 2):
            if not all(focus_values[i:i+2]):
                continue
            if sum(focus_values[i:i+2]) != 100:
                msg = f"The sum of {focus_fields[i].split('_', 1)[1]} and " \
                    f"{focus_fields[i+1].split('_', 1)[1]} must be equal " \
                    f"to 100."
                self.add_error(focus_fields[i], msg)
                self.add_error(focus_fields[i+1], msg)

        if total_supply and proposal and proposal > total_supply:
            self.add_error(
                'stocks_quantity_proposal',
                "Quantity proposed can't be higher than the total supply."
                )

        if pos_supply and pos_proposal and pos_proposal > pos_supply:
            self.add_error(
                'end_product_or_service_quantity_proposal',
                "Quantity proposed can't be higher than the total supply."
                )

        return cleaned_data


# COMMENT FORM
class NoteForm(forms.ModelForm):
    """
    Form for creating or updating a comments on posts.
    It includes a single field for the content.
    """

    # CUSTOM INPUT TYPES & PLACEHOLDER
    content_note = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Share your opinion or place a public offer'}
            )
    )

    class Meta:
        model = Note
        fields = [
            'content_note',
        ]
