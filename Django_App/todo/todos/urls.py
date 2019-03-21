from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.home, name="home"),
    path('todo/<int:todo_id>/complete/', views.complete, name="complete"),
    path('todo/<int:todo_id>/edit/', views.edit, name="edit"),
    path('todo/<int:todo_id>/delete/', views.delete, name="delete"),
]
