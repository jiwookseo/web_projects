from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutForm, ShoutModelForm

# Create your views here.
def home(request):
    if request.method=="POST":
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            shout = form.save(commit=False)
            shout.user = request.user
            shout.save()
        return redirect('shouts:home')
    else:
        form = ShoutModelForm()
        return render(request, 'shouts/home.html', {'form':form})

def edit(request, shout_id):
    shout = Shout.objects.get(id=shout_id)
    if request.method=="POST":
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            pass
        return redirect('shouts:home')
    else:
        form = ShoutModelForm(instance=shout)
        return render(request, 'shouts/edit.html', {'form':form})
        
def delete(request, shout_id):
    if request.method=="POST":
        shout = Shout.objects.get(id=shout_id)
        shout.delete()
    return redirect('shouts:home')