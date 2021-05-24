from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_list,name="todolist"),
    path('<int:id>/',views.todo_detail,name="todo_detail"),
    path('create/',views.todo_create,name="create"),
    path('<int:id>/update/',views.todo_update,name="update"),
    path('<int:id>/delete/',views.todo_delete,name="delete"),
]