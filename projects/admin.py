from django.contrib import admin
from .models import Post, Note, Register, Profile, Feedback
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):

    list_display = ('username',)
    list_filter = ('username',)
    search_fields = ('username',)


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('username', 'company', 'occupation', 'email')
    search_fields = ['username', 'location', 'company']
    list_filter = ('location', 'last_name', 'company', 'email', 'occupation')
    summernote_fields = ('bio',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('industry', 'author', 'created_on', 'status')
    search_fields = ['content', 'industry', 'author', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'industry', 'updated_on')
    summernote_fields = ('content', 'decription')


@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('name', 'note', 'created_on_note', 'approved')
    list_filter = ('name', 'note', 'approved', 'created_on_note')
    search_fields = ('name', 'email', 'username' 'content_note')
    actions = ['approved_note']

    def approved_note(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Feedback)
class FeedbackAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'feedback')
    search_fields = ['name', 'email']
    list_filter = ('name', 'email', 'feedback')
    summernote_fields = ('feedback')
