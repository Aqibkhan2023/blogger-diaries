from django.contrib import admin
from django.urls import path, include
from froala_editor import views
from api.api import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
    path('blogs/', BlogView.as_view(), name='blogs',),
    path('blogs/<int:id>', BlogDetailView.as_view(), name = 'blog_details'),
    path('comments/<int:blog_id>', CommentView.as_view(), name='comments',),
    # path('comments/<int:id>', CommentDetailView.as_view(), name = 'comment_details'),
]
