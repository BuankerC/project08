from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('genres/', views.genres, name="genres"),
    path('genres/<int:id>/', views.genres_id, name="genres_id"),
    path('movies/', views.movies),
    path('movies/<int:id>/', views.movies_id),
    path('movies/<int:id>/scores/', views.movies_score),
    path('scores/<int:id>', views.scores_id),
]
