from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home'),
    path('create-profile', views.UserProfileCreate.as_view(), name='create_profile'),
    path('my-profile', views.get_user_profile, name='view_profile'),
    path('projects/', views.PostList.as_view(), name='all_projects'),
    path('projects/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    path('create-project', views.create_post, name='post_create'),
    path('my-projects', views.get_user_posts, name='user_posts'),
    path('contact', views.contact_page, name='contact'),
]
