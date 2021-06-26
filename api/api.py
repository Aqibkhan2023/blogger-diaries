from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from .models import Blog, Comment
from rest_framework.pagination import PageNumberPagination
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers


class BlogView(APIView):
    def get(self, request):
        queryset = Blog.objects.all().filter(publishedAt__isnull=False).order_by("-publishedAt")[:3]
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BlogDetailView(APIView):
    def get(self, request, id):
        blog = Blog.objects.get(pk=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

class CommentView(APIView):
    def get(self, request, blog_id):
        queryset = Comment.objects.all().filter(blog = blog_id).order_by("-timePosted")[:100]
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, blog_id):
        commentDetails = request.data.copy()
        commentDetails['blog'] = blog_id
        serializer = CommentSerializer(data=commentDetails)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CommentDetailView(APIView):
    def get(self, request, id):
        comment = Comment.objects.get(pk = id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
        
class AppBlogListView(APIView): # Pagination
    def get(self, request, pageno):
        pageno = int (pageno)
        page_size = 5
        queryset = Blog.objects.all().order_by("-publishedAt")[page_size*pageno: page_size*pageno + page_size]
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)