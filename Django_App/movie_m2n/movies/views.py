from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Score
from .forms import ScoreForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies': movies})


def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = ScoreForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'form': form})


@login_required
@require_POST
def new_score(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = ScoreForm(request.POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.user = request.user
        score.movie = movie
        score.save()
    else:
        return render(request, 'movies/detail.html', {'movie': movie, 'form': form})
    return redirect('movies:detail', pk=pk)


@login_required
@require_POST
def delete_score(request, movie_pk, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if request.user == score.user:
        score.delete()
    return redirect('movies:detail', pk=movie_pk)
