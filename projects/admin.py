from django.contrib import admin
from .models import Post, Note
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('name', 'content_note', 'note', 'created_on_note', 'approved')
    list_filter = ('approved', 'created_on_note')
    search_fields = ('name', 'email', 'content_note')
    actions = ['approved_note']

    def approved_note(self, request, queryset):
        queryset.update(approved=True)
