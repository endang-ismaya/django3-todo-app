from django.shortcuts import redirect, render
from .models import SingleTodo
from .forms import SingleTodoForm

# Create your views here.
def index(request):
    todos = SingleTodo.objects.all()
    context = {"todos": todos}
    return render(request, "app_todo/index.html", context=context)


def add_todo(request):

    if request.method == "POST":
        form = SingleTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_todo_index")
    else:
        form = SingleTodoForm()

    return render(request, "app_todo/add-todo.html", {"form": form})


def update_todo(request, todo_id):
    todo = SingleTodo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("app_todo_index")


def delete_todo(request, todo_id):
    SingleTodo.objects.filter(id=todo_id).delete()
    return redirect("app_todo_index")


def about_page(request):
    return render(request, "app_todo/about.html")
