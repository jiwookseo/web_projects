from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie, Score
from .serializers import GenreSerializer, MovieSerializer, ScoreSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    # try:
    #     genre = Genre.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # try:
    #     movie = Movie.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    

@api_view(['POST'])
def movie_score(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # try:
    #     movie = Movie.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ScoreSerializer(data=request.data, context={'movie':pk})
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def score_detail(request, pk):
    score = get_object_or_404(Score, pk=pk)
    # try:
    #     score = Score.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ScoreSerializer(score, data=request.data, context={'movie':pk})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        score.delete()
        return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
