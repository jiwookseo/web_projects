from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == "POST":
        # authentication
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # authorization and redirect
        if user: # authentication success
            login(request, user)
            # login success msg
            messages.success(request, 'Login Success')
            return redirect('todos:home')
        else: # authentication fail
            # login fail msg
            messages.success(request, 'Login Fail, check your username & password')
            return redirect('users:login')
    else:
        return render(request, 'users/login.html')
        
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('todos:home')
    
def profile(request):
    return render(request, 'users/profile.html')
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Success, welcome {}'.format(form.instance.username))
            login(request, form.instance)
            return redirect('todos:home')
        else:
            messages.success(request, 'Register Fail, check yout input')
            return redirect('users:register')
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})