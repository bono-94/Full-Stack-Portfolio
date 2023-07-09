from . import views
from django.urls import path
from .views import *


urlpatterns = [
    # INFO
    path('', views.home_page, name='home'),
    # ABOUT
    path('about', views.about_page, name='about'),
    # PROFILE
    path('my-profile/', views.user_profile, name='user_profile'),
    path('my-profile/edit', views.edit_profile, name='edit_profile'),
    path('my-profile/delete/', views.delete_profile, name='delete_profile'),
    path('public-profile/<user_profile>', views.view_public_profiles, name='public_profile'),
    # POST PUBLIC
    path('posts/', views.PostList.as_view(), name='public_posts_list'),
    path('posts/<slug:slug>', views.PostDetail.as_view(), name='public_post_details_1_landing'),
    path('posts/<slug:slug>/details', views.PostDetailOpps.as_view(), name='public_post_details_2_opps'),
    path('posts/<slug:slug>/about-us', views.PostDetailAboutUs.as_view(), name='public_post_details_3_about_us'),
    path('posts/<slug:slug>/body', views.PostDetailBody.as_view(), name='public_post_details_4_body'),
    path('posts/<slug:slug>/files', views.PostDetailFiles.as_view(), name='public_post_details_5_files'),
    path('posts/<slug:slug>/proposal', views.PostDetailProposal.as_view(), name='public_post_details_6_proposal'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    # POST PRIVATE
    path('my-posts', views.UserPosts.as_view(), name='user_posts_list'),
    path('create-post', views.PostCreate.as_view(), name='user_post_create'),
    path('my-posts/edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('my-posts/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    # REQUEST
    path('request', views.SupportRequest.as_view(), name='request'),
]
