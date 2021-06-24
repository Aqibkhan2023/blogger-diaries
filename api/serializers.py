from rest_framework import serializers
from . import models

class BlogSerializer(serializers.Serializer):
    model = models.Blog
    fields = [
        'title',
        'slug',
        'authorName',
        'content',
        'category',
        'createdAt',
        'publishedAt',
        'lastEdited'        
    ]

class CommentSerializer(serializers.Serializer):
    model = models.Comment
    fields = [
        'userName',
        'content',
        'timePosted',
        'blog'        
    ]
class CategorySerializer(serializers.Serializer):
    model = models.Category
    fields = [
        'title',  
    ]

class ImageSerializer(serializers.Serializer):
    model = models.Image
    fields = [
        '`name`',
        'imageData',
        'imageType',
        'blog'  
    ]
