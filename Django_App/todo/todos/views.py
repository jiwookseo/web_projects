from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        Todo.objects.create(content=request.POST.get('content'), user=request.user)
        return redirect('todos:home')
    else:
        return render(request, 'todos/home.html')

def complete(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.completed = False if todo.completed else True
        todo.save()
    return redirect('todos:home')

def delete(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
    return redirect('todos:home')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.content = request.POST.get('content')
        todo.save()
        return redirect('todos:home')
    else:
        return render(request, 'todos/edit.html', {'todo':todo})
        
