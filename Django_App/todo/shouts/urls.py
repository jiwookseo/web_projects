from django.urls import path
from . import views

app_name = 'shouts'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:shout_id>/edit/', views.edit, name="edit"),
    path('<int:shout_id>/delete/', views.delete, name="delete"),
]
