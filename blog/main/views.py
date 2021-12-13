from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from . import permissions as my_permissions


class CharFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    category = CharFilter(field_name='category__title')

    class Meta:
        model = Post
        fields = ['category']


class PostListView(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend, )
    permission_classes = [permissions.AllowAny]
    filterset_class = PostFilter
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (my_permissions.IsAuthor, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostDeleteView(generics.DestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated, )
#     serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





# class CategoryListView(generics.ListAPIView):
#     permission_classes = [permissions.AllowAny]
#
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryDetailView(generics.RetrieveAPIView):
#
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryCreateView(generics.CreateAPIView):
#     # queryset = Category.objects.all()
#     serializer_class = CategorySerializer




