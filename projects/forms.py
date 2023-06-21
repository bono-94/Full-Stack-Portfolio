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
            # POST LIST DESING
            'post_list_description',
            'post_list_image',
            # POST STRUCTURE
            'public_privacy',
            'post_background_audio',
            'post_colors_list',
            'post_color_primary',
            'post_color_secondary',
            'post_color_text',
            # POST INTRODUCTION
            'post_logo_image',
            'post_banner_image',
            'title',
            'caption',
            'project_owner',
            'industry',
            'post_type',
            'organization',
            'project',
            'product',
            'service',
            'post_location_city',
            'post_location_country',
            'post_location_continent',
            'post_location_planet',
            'launch_date',
            'end_date',
            'infinite_end_date',
            'introduction',
            # POST PITCH VIDEO
            'post_video_privacy',
            'post_video',
            # POST ABOUT
            'post_about_privacy',
            'organization_info',
            'organization_culture',
            'organization_mission',
            'organization_vision',
            'products_provided',
            'services_provided',
            'pps_objectives',
            'pps_goals',
            'pps_milestones',
            'team',
            'partners',
            'collaborators',
            'sponsors',
            'community',
            'stakeholders',
            'shareholders',
            'resources_requiered',
            'target_markets',
            'target_group',
            'values_provided',
            'differentiation',
            'sdg_goals',
            'intellectual_property',
            'legal_protection',
            'licencing',
            'franchizing',
            'risks',
            'challenges',
            'change',
            'impact',
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
            # POST BODY
            'post_body_privacy',
            'main_content',
            'business_knowledge',
            'story',
            'journey',
            'future',
            'legacy',
            # POST BRIDGE
            'post_bridge_privacy_library',
            'post_bridge_privacy_documents',
            # POST BRIDGE - BUSINESS LIBRARY
            'organizational_structure',
            'flowchart',
            'agenda',
            'timeline',
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
            'business_plan',
            'implementation_plan',
            'pestle_report',
            'internal_report',
            'business_plan',
            'business_model_canvas',
            'contracts',
            'terms_conditions',
            # POST CONCLUSION
            'post_conclusion_privacy',
            'post_fee_model_privacy',
            'fee_model',
            'offer_model',
            'amount_requested',
            'payout_date',
            'stocks_offering',
            'stocks_supply',
            'ownership_percentage',
            'return_amount',
            'end_product_or_service_quality',
            'end_product_or_service_quantity',
            'lifetime_discount_percentages',
            'team_guaranteed_position',
            'partnership',
            'collaboration',
            'sponsorship',
            'community_access',
            'pioneering',
            'merchandize',
            'special_acknowledgement',
            'open_offers',
            'offer_terms',
            # POST CONTACT
            'post_contact_privacy',
            'post_public_email',
            'public_phone',
            'contact_days',
            'contact_hours',
            'website_link',
            'facebook_link',
            'twitter_link',
            'instagram_link',
            'linkedin_link',
            'youtube_link',
            # POST EVENT
            'event_color',
            'event_image',
            'event_link',
            'event_title',
            'event_host',
            'event_content',
            'event_date',
            'event_hour',
            'event_minute',
            'event_location',
            'event_price',
            'event_price_cents',
            'event_capacity',
            # POST RESULTS
            'post_results_privacy',
            'number_of_phases',
            'amount_asked',
            'amount_collected',
            'ownership_offered',
            'ownerhip_given',
            'team_positions_offered',
            'team_positions_given',
        ]

        # CUSTOM INPUT TYPES
        widgets = {
            'post_color_primary': forms.TextInput(attrs={'type': 'color'}),
            'post_color_secondary': forms.TextInput(attrs={'type': 'color'}),
            'event_color': forms.TextInput(attrs={'type': 'color'}),
            'launch_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
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
