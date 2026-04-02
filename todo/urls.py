from django.urls import path 
from .views import home, contact, home2, todo, todo_create, todo_edit, todo_mark, todo_delete

urlpatterns=[

    path('home/', home),
    path('contact/', contact), 
    path('home2/', home2), 
    path('todo/', todo),
    path('todo/create/', todo_create),
    path('todo/edit/<id>/', todo_edit),
    path('todo/mark/<id>/', todo_mark),
    path('todo/delete/<id>/', todo_delete),
    

]