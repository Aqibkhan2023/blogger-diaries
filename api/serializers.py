from rest_framework import serializers
from . import models
from django.utils.text import slugify

class BlogSerializer(serializers.ModelSerializer):
    # category = serializers.RelatedField(read_only=True)

    class Meta:
        model = models.Blog
        fields = (
            'title',
            'authorName',
            'content',
            'category',
            'slug',
            'createdAt',
            'publishedAt',
            'lastEdited'        
        )
    def create(self, validated_data):
        return models.Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.lastEdited = validated_data.get('lastEdited', instance.lastEdited)
        instance.publishedAt = validated_data.get('publishedAt', instance.publishedAt)
        instance.authorName = validated_data.get('authorName', instance.authorName)
        instance.category = validated_data.get('category', instance.category)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'userName',
            'content',
            'timePosted',
            'blog'        
        )
    def create(self, validated_data):
        return models.Comment.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            'title',  
        )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'name',
            'imageData',
            'imageType',
            'blog'  
        )
