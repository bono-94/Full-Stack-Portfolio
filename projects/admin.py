from django.contrib import admin
from .models import Post, Notes
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('name', 'content_notes', 'note', 'created_on_notes', 'approved')
    list_filter = ('approved', 'created_on_notes')
    search_fields = ('name', 'email', 'content_notes')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
