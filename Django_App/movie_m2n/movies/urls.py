from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/scores/new', views.new_score, name='new_score'),
    path('<int:movie_pk>/scores/<int:score_pk>/delete', views.delete_score, name='delete_score'),
]
