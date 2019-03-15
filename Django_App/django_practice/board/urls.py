from django.urls import path
from . import views
app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_new, name='new'),
    path('<int:article_id>/', views.article_detail, name="detail"),
    path('<int:article_id>/comment/', views.article_comment_create, name="comment_create"),
    path('<int:article_id>/comment/<int:comment_id>', views.article_comment_delete, name="comment_delete"),
    path('<int:article_id>/update/', views.article_update, name="update"),
    path('<int:article_id>/delete/', views.article_delete, name="delete"),
]