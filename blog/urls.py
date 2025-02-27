from django import urls
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('contact/', views.contact, name='blog_contact'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),     # ✅ تأكد من استخدام `int:post_id`
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/', views.all_posts, name='posts'),
]
