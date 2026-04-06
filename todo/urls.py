from django.urls import path 
from .views import first, home, contact, home2, todo, todo_create, todo_edit, todo_mark, todo_delete, todo_display, todo_welcome

urlpatterns=[
    
    path('first/', first),
    path('home/', home),
    path('contact/', contact), 
    path('home2/', home2), 
    path('todo/', todo),
    path('todo/create/', todo_create),
    path('todo/edit/<id>/', todo_edit),
    path('todo/mark/<id>/', todo_mark),
    path('todo/delete/<id>/', todo_delete),
    
    path('api/todo/welcome/', todo_welcome),
    path('api/todo/display/', todo_display),
    

]