from django.contrib import admin
from .models import Post, Note, Profile, Request
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


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'username', 'public_email', 'location', 'organization', 'occupation')
    search_fields = ['first_name', 'last_name', 'username', 'public_email', 'location', 'organization', 'occupation']
    prepopulated_fields = {'slug': ('username',)}
    list_filter = ('first_name', 'last_name', 'username', 'public_email', 'location', 'organization', 'occupation')
    summernote_fields = ('bio')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('industry', 'author', 'created_on', 'status')
    search_fields = ['main_content', 'industry', 'author', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'industry', 'updated_on')
    summernote_fields = ('main_content', 'decription')


@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('name', 'note', 'created_on_note', 'approved')
    list_filter = ('name', 'note', 'approved', 'created_on_note')
    search_fields = ('name', 'email', 'username', 'content_note')
    actions = ['approved_note']

    def approved_note(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Request)
class RequestAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    list_filter = ('name', 'email')
    summernote_fields = ('request')
