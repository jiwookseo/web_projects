from django.shortcuts import render, redirect
from .models import Movie, Genre, Score


def movie_list(request):
    movies = Movie.objects.order_by('-id')
    return render(request, 'movies/list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


def movie_delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('movies:movie_list')
    else:
        return redirect('movies:movie_detail', movie_id)


def movie_update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.description = request.POST.get('description')
        movie.genre_id = request.POST.get('genre')
        movie.poster_url = request.POST.get('poster_url')
        movie.save()
        return redirect('movies:movie_detail', movie_id)
    else:
        return render(request, 'movies/update.html', {'movie': movie, 'genres': Genre.objects.all()})


def score_new(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        score = Score(
            content=request.POST.get('content'),
            score=request.POST.get('score'),
            movie=movie
        )
        score.save()
    return redirect('movies:movie_detail', movie_id)


def score_delete(request, movie_id, score_id):
    if request.method == 'POST':
        score = Score.objects.get(id=score_id)
        score.delete()
    return redirect('movies:movie_detail', movie_id)
