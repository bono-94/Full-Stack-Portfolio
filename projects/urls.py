from . import views
from django.urls import path
from .views import *


urlpatterns = [
    # INFO
    path('', views.home_page, name='home'),
    path('extra', views.final, name='home'),
    # ABOUT
    path('about', views.about_page, name='about'),
    # PROFILE
    path('my-profile/', views.user_profile, name='user_profile'),
    path('my-profile/edit', views.edit_profile, name='edit_profile'),
    path('my-profile/delete/', views.delete_profile, name='delete_profile'),
    path('profile/<user_profile>', views.view_public_profiles, name='public_profile'),
    # POST
    path('create-project', views.PostCreate.as_view(), name='post_create'),
    path('projects/', views.PostList.as_view(), name='all_projects'),
    path('projects/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    path('my-projects', views.UserPosts.as_view(), name='user_posts'),
    path('post/edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    # REQUEST
    path('request', views.SupportRequest.as_view(), name='request'),
]
