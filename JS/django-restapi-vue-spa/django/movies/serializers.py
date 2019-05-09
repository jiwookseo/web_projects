from rest_framework import serializers
from .models import Genre, Movie, Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'
