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
        # PROFILE COLOR AS COLORPICKER
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
            'post_list_image',
            'title',
            'caption',
            'industry',
            'organization',
            'main_content',
        ]


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
