from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/follow', views.follow, name='follow'),
    path('<int:pk>/followers', views.follower, name='follower'),
    path('<int:pk>/followings', views.following, name='following'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
