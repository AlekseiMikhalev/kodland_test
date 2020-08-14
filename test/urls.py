from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('article/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPost.as_view(), name='create'),]