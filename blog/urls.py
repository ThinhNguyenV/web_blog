from django.urls import path
from .views import register
from .views import post_list, post_detail, post_new, post_edit, post_delete, add_comment_to_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('register/', register, name='register'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
]
