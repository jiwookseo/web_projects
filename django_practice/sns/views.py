from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment


def posting_list(request):
    if request.method == 'POST':
        posting = Posting(
            content=request.POST.get('content'),
            icon=request.POST.get('icon'),
            image=request.FILES.get('image'),
        )
        posting.save()
        return redirect('sns:posting_detail', posting.id)
    else:
        postings = Posting.objects.order_by('-updated_at')
        return render(request, 'sns/list.html', {
            'postings': postings
        })


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.order_by('-created_at')  # TODO: Duck-typing
    return render(request, 'sns/detail.html', {
        'posting': posting,
        'comments': comments
    })


def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        comment = Comment(
            posting=posting,
            content=request.POST.get('content')
        )
        comment.save()
    return redirect('sns:posting_detail', posting_id)
