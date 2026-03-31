from django.urls import path 
from .views import home, contact, home_extends, todo

urlpatterns=[

    path('home/', home),
    path('contact/', contact), 
    path('home_extends/', home_extends), 
    path('todo/', todo)

]