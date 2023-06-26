from django import forms
from .models import Profile, Post, Note, Request
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            # PUBLIC VISIBILITY
            'privacy',
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
            'current_employment_privacy',
            'industry',
            'organization',
            'department',
            'occupation',
            'start_date',
            'hours_per_week',
            # CAREER
            'history_employment_privacy',
            'cv',
            'education',
            'work_history',
            'projects_portfolio',
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

    def clean(self):

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
                msg = f"The sum of {focus_fields[i].split('_', 1)[1]} and {focus_fields[i+1].split('_', 1)[1]} must be equal to 100."
                self.add_error(focus_fields[i], msg)
                self.add_error(focus_fields[i+1], msg)
        return cleaned_data


class PostForm(forms.ModelForm):
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
            'same_start_launch_date',
            # POST OPPS SPECIFICS
            'post_opps_details_privacy',
            'pps_vision',
            'pps_goals',
            'pps_missions',
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
            'products_provided',
            'services_provided',
            'organization_mission',
            'organization_vision',
            'organization_culture',
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
            'special_ops',
            'special_finance',
            'special_marketing',
            'special_supply_chain',
            'special_hr',
            'special_tech',
            'special_sustainability',
            'special_research',
            'specialty_privacy_two',
            'special_ops_two',
            'special_finance_two',
            'special_marketing_two',
            'special_supply_chain_two',
            'special_hr_two',
            'special_tech_two',
            'special_sustainability_two',
            'special_research_two',
            'percentage_special_privacy',
            'percentage_special_ops',
            'percentage_special_ops_two',
            'percentage_special_finance',
            'percentage_special_finance_two',
            'percentage_special_marketing',
            'percentage_special_marketing_two',
            'percentage_special_supply_chain',
            'percentage_special_supply_chain_two',
            'percentage_special_hr',
            'percentage_special_hr_two',
            'percentage_special_tech',
            'percentage_special_tech_two',
            'percentage_special_sustainability',
            'percentage_special_sustainability_two',
            'percentage_special_research',
            'percentage_special_research_two',
            # POST BODY
            'post_body_privacy',
            'main_content',
            'business_knowledge',
            'story',
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
            'funding_start_date',
            'funding_end_date',
            'funding_infinite_end_date',
            'funding_payout_date',
            'stocks_quantity_total_supply',
            'stocks_quantity_proposal',
            'stocks_proposal_note',
            'stocks_proposal_return',
            'ownership_percentage_opps_type',
            'ownership_percentage_opps_quantity_proposal',
            'ownership_percentage_opps_proposal_note',
            'ownership_percentage_opps_proposal_return',
            'end_product_or_service_type',
            'end_product_or_service_total_supply',
            'end_product_or_service_quantity_proposal',
            'end_product_or_service_merch_proposal',
            'end_product_or_service_membership_proposal',
            'end_product_or_service_proposal_note',
            'end_product_or_service_proposal_return',
            'lifetime_discount_percentages_quantity_proposal',
            'lifetime_discount_percentages_quality_proposal_note',
            'lifetime_discount_percentages_proposal_return',
            'team_guaranteed_position_title_proposal',
            'team_guaranteed_responsibilities_proposal',
            'team_guaranteed_employment_conditions_proposal',
            'team_guaranteed_proposal_return',
            'partnership_proposal',
            'partnership_proposal_return',
            'collaboration_proposal',
            'collaboration_proposal_return',
            'sponsorship_proposal',
            'sponsorship_proposal_return',
            'open_proposal',
            'open_proposal_proposal_return',
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
                msg = f"The sum of {focus_fields[i].split('_', 1)[1]} and {focus_fields[i+1].split('_', 1)[1]} must be equal to 100."
                self.add_error(focus_fields[i], msg)
                self.add_error(focus_fields[i+1], msg)
        return cleaned_data


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'content_note',
        ]


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'name',
            'email',
            'request',
        ]
