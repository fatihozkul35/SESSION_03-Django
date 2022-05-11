from django.urls import path
from .views import (
    home,
    list_todo,
    todo_create,
    HomeView,
    TodoListView,
    TodoCreateView
)

urlpatterns = [
    path('', home, name='home'),
    # path('', HomeView.as_view(template_name='todo_app/home.html'), name='home'),
    # path('list/', list_todo, name='list-todo'),
    path('list/', TodoListView.as_view(), name='list-todo'),
    # path('create/', todo_create, name='create-todo'),
    path('create/', TodoCreateView.as_view(), name='create-todo'),
]
