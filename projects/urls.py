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
    # path('my-project/detail', views.user_projects, name='user_project'),
    # path('my-projects/<slug:slug>', views.UserPostDetail().as_view(), name='user_post_detail'),
    # path('vote/<slug:slug>', views.UserPostVote.as_view(), name='vote'),
    # path('my-project/edit', views.edit_project, name='edit_project'),
    # path('my-project/delete/', views.delete_project, name='delete_project'),
    #
    path('contact', views.contact_page, name='contact'),
    #
    path('request', views.SupportRequest.as_view(), name='request'),
    # path('create/', post_create, name='post_create'),
    # path('update/<slug:slug>/', post_update, name='project_update'),
    # path('delete/<slug:slug>/', post_delete, name='post_delete'),
    # path('', post_list, name='post_list'),
    # path('<slug:slug>/', post_detail, name='post_detail'),
]
