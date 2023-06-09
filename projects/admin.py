"""
Admin configuration for managing models in the Django admin site.
This file registers models and customizes the admin interface.
"""

from django.contrib import admin
from .models import Post, Note, Profile
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profiles'
    fk_name = 'username'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# PROFILE ADMIN
@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'username',
        'public_email',
        'location',
        'organization',
        'occupation',
    )
    search_fields = [
        'first_name',
        'last_name',
        'username',
        'public_email',
        'location',
        'organization',
        'occupation',
    ]
    prepopulated_fields = {'slug': ('username',)}
    list_filter = (
        'first_name',
        'last_name',
        'username',
        'public_email',
        'location',
        'organization',
        'occupation',
    )
    summernote_fields = ('bio',)


# POST ADMIN
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = (
        'post_type',
        'title',
        'industry',
        'author',
        'created_on',
        'status',
        'post_verification',
    )

    search_fields = [
        'title',
        'caption',
        'author',
        'project_owner',
        'organization',
        'project',
        'product',
        'service',
        'post_location_city',
        'post_location_country',
        'post_location_continent',
        'post_location_planet',
        'business_knowledge',
    ]

    list_filter = (
        'status',
        'post_verification',
        'public_privacy',
        'post_type',
        'funding_infinite_end_date',
    )

    summernote_fields = (
        'business_knowledge',
        'caption',
        'introduction'
    )

    prepopulated_fields = {'slug': ('title',)}

    # ACTIONS
    actions = ['approved_post', 'frozen_post']

    def approved_post(self, request, queryset):
        queryset.update(status=1)

    def frozen_post(self, request, queryset):
        queryset.update(status=0)


# NOTES ADMIN
@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('content_note', 'note', 'created_on_note', 'approved')
    list_filter = ('content_note', 'note', 'approved', 'created_on_note')
    search_fields = ('content_note', 'email', 'content_note')

    # ACTIONS
    actions = ['approved_note']

    def approved_note(self, request, queryset):
        queryset.update(approved=True)
