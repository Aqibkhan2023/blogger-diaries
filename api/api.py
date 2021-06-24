from django.http import JsonResponse
from django.shortcuts import render

from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.all().filter(publishedAt__isnull=False).order_by("-publishedAt")[:3]
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BlogDetailView(APIView):
    def get(self, request,  *args, **kwargs):
        blog = Blog.objects.get(pk=self.kwargs['id'])
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Comment.objects.all().filter(blog = self.kwargs['blog_id']).order_by("-timePosted")[:100]
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        commentDetails = request.data
        commentDetails['blog'] = self.kwargs['blog_id']
        serializer = CommentSerializer(data=commentDetails)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# class CommentDetailView(APIView):
#     def get(self, request,  *args, **kwargs):
#         blog = Blog.objects.get(pk=self.kwargs['id'])
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
        