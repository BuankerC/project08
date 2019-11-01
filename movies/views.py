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
        