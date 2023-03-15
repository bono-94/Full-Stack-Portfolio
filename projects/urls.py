from . import views
from django.urls import path
from templates.views import get_posts_list


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('vote/<slug:slug>', views.PostVote.as_view(), name='vote'),
    path('post-create', views.PostCreate.as_view(), name='post_create'),
]