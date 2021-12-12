from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('post/create/', views.PostCreateView.as_view()),

    path('category/', views.CategoryListView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailView.as_view()),  #????????????
    path('category/create/', views.CategoryCreateView.as_view()),
]