from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', views.home_page, name='home'),
    path('create-profile', views.ProfileCreate.as_view(), name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('profile/view/', views.view_profile, name='view_profile'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/register/', CustomSignupView.as_view(), name='account_register'),
    # path('profile/<str:username>/', views.view_profile, name='view_profile'),
    # path('profile/', views.view_profile, name='view_profile'),
    # path('profile/edit/', views.edit_profi
    # le, name='edit_profile'),
    # path('profile/delete/', views.delete_profile, name='delete_profile'),
    # path('my-profile/', views.ProfileView.as_view(), name='view_profile'),
    # path('edit/<int:pk>', views.ProfileEdit.as_view(), name='edit_profile'),
    # path('delete/<int:pk>', views.ProfileDelete.as_view(), name='delete_profile'),
    path('projects/', views.PostList.as_view(), name='all_projects'),
    path('projects/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    path('my-projects/none', views.UserPostsNone.as_view(), name='user_posts_none'),
    path('my-projects', views.UserPosts.as_view(), name='user_posts'),
    path('create-project', views.PostCreate.as_view(), name='post_create'),
    path('edit-project', views.PostEdit.as_view(), name='post _edit'),
    path('delete-project', views.PostDelete.as_view(), name='post_delete'),
    path('contact', views.contact_page, name='contact'),
    path('feedback', views.FeedbackSend.as_view(), name='feedback'),
]
