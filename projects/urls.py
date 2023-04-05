from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', views.home_page, name='home'),
    #
    path('my-profile/', views.user_profile, name='user_profile'),
    path('my-profile/edit', views.edit_profile, name='edit_profile'),
    path('my-profile/delete/', views.delete_profile, name='delete_profile'),
    #
    path('projects/', views.PostList.as_view(), name='all_projects'),
    path('projects/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    #
    path('my-projects/none', views.UserPostsNone.as_view(), name='user_posts_none'),
    path('my-projects', views.UserPosts.as_view(), name='user_posts'),
    path('create-project', views.PostCreate.as_view(), name='post_create'),
    path('edit-project', views.PostEdit.as_view(), name='post _edit'),
    path('delete-project', views.PostDelete.as_view(), name='post_delete'),
    #
    path('contact', views.contact_page, name='contact'),
    #
    path('feedback', views.FeedbackSend.as_view(), name='feedback'),
]
