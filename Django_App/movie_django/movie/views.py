from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    return render(request,'movie/index.html',{'movies':movies})

def detail(request,pk):
    movie=Movie.objects.get(id=pk)
    return render(request,'movie/detail.html',{'movie':movie})
    
def edit(request,pk):
    movie=Movie.objects.get(id=pk)
    return render(request,'movie/edit.html',{'movie':movie})
    
def update(request,pk):
    movie=Movie.objects.get(id=pk)
    movie.title=request.POST.get('title')
    movie.audience=request.POST.get('audience')
    movie.genre=request.POST.get('genre')
    movie.score=request.POST.get('score')
    movie.poster_url=request.POST.get('poster_url')
    movie.description=request.POST.get('description')
    movie.save()
    return redirect('detail', pk)
    
def delete(request,pk):
    movie=Movie.objects.get(id=pk)
    movie.delete()
    return redirect('index')