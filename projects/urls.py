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
    path('my-projects/none', views.no_posts_user, name='user_posts_none'),
    path('create-project', views.PostCreate.as_view(), name='post_create'),
    path('my-projects', views.UserPosts.as_view(), name='user_posts'),
    #
    path('contact', views.contact_page, name='contact'),
    #
    path('request', views.SupportRequest.as_view(), name='request'),

]
