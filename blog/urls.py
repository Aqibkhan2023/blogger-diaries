from django.contrib import admin
from django.urls import path, include
from api.api import BlogView, BlogDetailView, AppBlogListView, CommentView, CommentDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', BlogView.as_view(), name='blogs',),
    path('blogs/<id>', BlogDetailView.as_view(), name = 'blog_details'),
    path('blogs_list/<pageno>/', AppBlogListView.as_view(), name = 'blog_paginated_list'),
    path('comments/<blog_id>', CommentView.as_view(), name='comments',),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('comments/details/<id>', CommentDetailView.as_view(), name = 'comment_details'),
] +  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
