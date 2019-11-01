# Project 08

##### Serializer활용

```python
from rest_framework import serializers
from .models import Movie, Genre, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id, ''title', 'audience', 'poster_url', 'description', 'genre_id',)

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source="movie_set", many=True)
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source="movie_set", many=True)
    movies_count = serializers.IntegerField(source="movie_set.count")
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies', 'movies_count',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        models = Review
        fields = ('id', 'content', 'score', 'movie_id',)
```



##### swagger 활용

```python
"""theater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Movie API",
        default_version='v1',
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
    path('redoc/', schema_view.with_ui('redoc')),
    path('swagger/', schema_view.with_ui('swagger')),
]

```



##### views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, Review
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, GenreSerializer, GenreDetailSerializer ,ReviewSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genres_id(request, id):
    genre = get_object_or_404(Genre, id=id)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movies_id(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = GenreDetailSerializer(Genre)
    return Response(serializer.data)

@api_view(['POST'])
def movies_score(request, id):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=id)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def scores_id(request, id):
    scores = get_object_or_404(Review, id=id)
    if request.method == "GET":
        serializer = ReviewSerializer(scores)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ReviewSerializer(data=request.data, instance=scores)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        scores.delete()
        return Response({'message':"삭제되었습니다!!!"})
```



