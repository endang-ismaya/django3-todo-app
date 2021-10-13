from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("", views.index, name="app_todo_index"),
    path("about/", views.about_page, name="app_todo_about"),
    path("add-todo/", views.add_todo, name="app_todo_add_todo"),
    path("update_todo/<int:todo_id>", views.update_todo, name="app_todo_upd_todo"),
    path("delete_todo/<int:todo_id>", views.delete_todo, name="app_todo_del_todo"),
]
