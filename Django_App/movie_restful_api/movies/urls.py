from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_swagger.views import get_swagger_view

app_name = 'movies'

urlpatterns = [
    path('docs/', get_swagger_view(title="API DOCS"), name="docs"),
    path('genres/', views.genre_list, name="genre_list"),
    path('genres/<int:pk>/', views.genre_detail, name="genre_detail"),
    path('movies/', views.movie_list, name="movie_list"),
    path('movies/<int:pk>/', views.movie_detail, name="movie_detail"),
    path('movies/<int:pk>/scores/', views.movie_score, name="movie_score"),
    path('scores/<int:pk>/', views.score_detail, name="score_detail"),
]
