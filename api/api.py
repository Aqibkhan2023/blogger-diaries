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
        



# #                                  Custom Pagination                                        #

# class CustomPagination(PageNumberPagination):
#     page_size = 10
#     def get_paginated_response(self, data):
#         return Response({
#             "status": True,
#             "code": status.HTTP_200_OK,
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.count,
#             'results': data
#         })
# class AppBlogListView(APIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     pagination_class = CustomPagination
#     def get(self, request):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)   