from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "memos"

urlpatterns = [
    path('', views.memos_list, name="memos_list"),
    path('<int:pk>/', views.delete_memo, name="delete_memo"),
]
