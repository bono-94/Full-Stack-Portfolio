from django import forms
from .models import Profile, Post, Note, Request


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            # PROFILE CARD
            'privacy',
            'profile_color',
            'profile_image',
            'profile_quote',
            'active_days',
            'active_hours',
            'website_link',
            'facebook_link',
            'twitter_link',
            'instagram_link',
            'linkedin_link',
            'youtube_link',
            # USER VIDEO
            'user_video',
            # GENERAL INFORMATION
            'public_email',
            'first_name',
            'last_name',
            'location',
            'languages',
            'gender',
            'date_of_birth',
            'height_cm',
            'weight_kg',
            # CURRENT EMPLOYMENT
            'industry',
            'company',
            'department',
            'occupation',
            'start_date',
            'hours_per_week',
            # PREVIOUS EMPLOYMENT
            'cv',
            'education',
            'work_history',
            'projects_portfolio',
            'references',
            'recommendations',
            # ACHIEVEMENTS
            'projects_completed',
            'goals_completed',
            'missions_completed',
            'milestones_completed',
            'tasks_completed',
            'contribution',
            # ATTRIBUTES
            'knowledge',
            'skills',
            'strengths',
            'weaknesses',
            # BUSINESS FOCUS
            'focus_innovation',
            'focus_financials',
            'focus_planning',
            'focus_monitoring',
            'focus_quality',
            'focus_quantity',
            'focus_collaboration',
            'focus_leadership',
            # BUSINESS SPECIALTY
            'special_ops',
            'special_finance',
            'special_marketing',
            'special_supply_chain',
            'special_hr',
            'special_tech',
            'special_sustainability',
            'special_research',
            # ACCOMPLISHMENTS
            'results',
            'certificates',
            'honors',
            'articles',
            'recognition',
            'bigger_fish_results',
            # REWARDS
            'awards',
            'business_rewards',
            'innovation_land_rewards',
            # PERSONAL WALL
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
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'project_image',
            'title',
            'description',
            'industry',
            'company',
            'content',
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
