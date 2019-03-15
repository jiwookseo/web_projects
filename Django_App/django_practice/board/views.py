from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from IPython import embed


def article_list(request):
    articles = Article.objects.order_by('-id').all()
    return render(request, 'board/list.html', {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.order_by('-id').all()
    if request.method == 'POST':
        article.like += 1
        article.save()
    return render(request, 'board/detail.html', {"article": article, "comments": comments})


def article_comment_create(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        comment = Comment(article=article, content=request.POST.get('content'))
        comment.save()
    return redirect('board:detail', article.id)


def article_comment_delete(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
    return redirect('board:detail', article.id)


def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
            article.delete()
            return redirect('board:list')


def article_new(request):
    if request.method == "POST":
        data = {"title": request.POST.get('title'), "content": request.POST.get('content')}
        article = Article(**data)
        article.save()
        return redirect('board:detail', article.id)
    elif request.method == "GET":
        return render(request, 'board/new.html')


def article_update(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:detail', article.id)
    elif request.method == "GET":
        article = Article.objects.get(id=article_id)
        return render(request, 'board/edit.html', {"article": article})
