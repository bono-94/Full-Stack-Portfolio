from django.contrib import admin
from .models import Post, Note, Register, Profile, Feedback
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'author')
    summernote_fields = ('content')


@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('name', 'content_note', 'note', 'created_on_note', 'approved')
    list_filter = ('approved', 'created_on_note')
    search_fields = ('name', 'email', 'content_note')
    actions = ['approved_note']

    def approved_note(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):

    list_display = ('username',)
    search_fields = ('username',)


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('username', 'company', 'occupation', 'email')
    search_fields = ['profile_title', 'username', 'location', 'company', 'email']
    list_filter = ('location', 'last_name', 'company', 'email', 'occupation')
    summernote_fields = ('bio',)


@admin.register(Feedback)
class FeedbackAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'feedback')
    search_fields = ['name', 'email']
    list_filter = ('name', 'email', 'feedback')
    summernote_fields = ('feedback')
