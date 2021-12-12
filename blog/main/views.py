from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class PostListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer




