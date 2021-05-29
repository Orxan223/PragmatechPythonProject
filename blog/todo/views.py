from django.shortcuts import render, redirect
from . models import Todo
from .forms import TodoForm

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    return render(request, "index.html",{'todos':todos})


def addTodo(request):
    if request.method == 'GET':
        return redirect("/")

    else:
        title = request.POST.get('title')
        newTodo = Todo(title = title)

        newTodo.save()
        return redirect("/")


def update(request, id):
    todo = Todo.objects.get(id=id)
    f = TodoForm(request.POST, request.FILES, instance=todo)
    if request.method == "POST":
        if f.is_valid():
            f.save()
            return redirect('index')
    context = {
        "f": f,
        "todo": todo

    }
    return render(request, "update.html", context)




def delete(request,id):
    todo = Todo.objects.filter(id=id).first()

    todo.delete()
    return redirect("/")
