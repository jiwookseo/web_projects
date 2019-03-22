from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MovieModelForm, ScoreModelForm

from .models import Movie, Genre, Score


def movie_list(request):
    movies = Movie.objects.order_by('-id')
    return render(request, 'movies/list.html', {'movies': movies})


def movie_new(request):
    if request.method == 'POST':
        form = MovieModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered')
            return redirect('movies:movie_detail', form.id)
        else:
            messages.success(request, 'Failed to register, check your input')
    else:
        form = MovieModelForm()
    return render(request, 'movies/form.html', {'form': form})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        form = ScoreModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully scored')
        else:
            messages.success(request, 'Failed to score, check your input')
            return render(request, 'movies/detail.html', {'movie': movie, 'form': form})
    form = ScoreModelForm(initial={'movie': movie})
    return render(request, 'movies/detail.html', {'movie': movie, 'form': form})


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
        form = MovieModelForm(instance=movie, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('movies:movie_detail', movie.id)
        else:
            messages.success(request, 'Failed to update, check your input')
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'movies/form.html', {'form': form})


def score_delete(request, movie_id, score_id):
    if request.method == 'POST':
        score = Score.objects.get(id=score_id)
        score.delete()
    return redirect('movies:movie_detail', movie_id)
