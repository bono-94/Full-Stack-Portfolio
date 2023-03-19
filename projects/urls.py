from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('projects/', views.PostList.as_view(), name='all_projects'),
    path('projects/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    path('post-create', views.create_post, name='post_create'),
    path('posts/<username>', views.UserPosts.as_view(), name='user_posts'),
    path('create-profile', views.UserProfileCreate.as_view(), name='create_profile'),
    path('<username>', views.UserProfileView.as_view(), name='view_profile'),
]
