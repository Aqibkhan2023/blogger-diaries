from django.contrib import admin

# Register your models here.
from .models import Blog, Comment, Image, Category
admin.register(Comment, Image, Category)(admin.ModelAdmin)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'authorName', 'publishedAt']
    list_filter = ['createdAt', 'publishedAt', 'title', 'authorName']
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publishedAt'

