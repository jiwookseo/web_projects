from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .forms import UserCustomCreationForm
from .models import User


def list(request):
    user = User.objects.all()
    return render(request, 'accounts/users.html', {'people': user, 'title': 'User List'})


def detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/detail.html', {'person': user})


@login_required
def follow(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user in request.user.from_user.all():
        request.user.from_user.remove(user)
    elif user != request.user:
        request.user.from_user.add(user)
    return redirect('accounts:detail', pk)


def follower(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/users.html',
                  {'people': user.to_user.all(), 'title': "{}'s Follower List".format(user.username)})


def following(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/users.html',
                  {'people': user.from_user.all(), 'title': "{}'s Following List".format(user.username)})


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
