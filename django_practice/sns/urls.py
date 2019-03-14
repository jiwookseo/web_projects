from django.urls import path
from . import views

app_name = 'sns'

urlpatterns = [
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>', views.posting_detail, name='posting_detail'),

    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'),
]
