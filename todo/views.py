from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos=Todo.objects.all()
    data={
        'todos':todos,
    }
    return render(request,"todolist.html",data)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    data={
        'todo':todo,
    }
    return render(request,"todo_detail.html",data)

def todo_create(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todolist')

    data={
        'form':form,
    }
    return render(request,'todo_create.html',data)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todolist')
    data={
        'form':form,
    }
    return render(request,'todo_update.html',data)

def todo_delete(request, id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("todolist")
    