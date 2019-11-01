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