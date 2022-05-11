from re import template
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Todo
from django.urls import reverse_lazy
from .forms import TodoAddForm, TodoUpdateForm


def home(request):
    return render(request, 'todo_app/home.html')


class HomeView(TemplateView):
    template_name = 'todo_app/home.html'


def list_todo(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "todo_app/todo_list.html", context)


class TodoListView(ListView):
    model = Todo
    # template_name = "todo_app/todo_list.html"  # app/models_list.html
    context_object_name = 'todos'  # object_list


def todo_create(request):
    # form = TodoAddForm()
    # if request.method == 'POST':
    #     form = TodoAddForm(request.POST)

    form = TodoAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list-todo")

    context = {
        'form': form
    }
    return render(request, 'todo_app/todo_create.html', context)


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoAddForm
    # fields = ('title')
    template_name = 'todo_app/todo_create.html'  # app/modelname_form.html
    success_url = reverse_lazy('list-todo')
