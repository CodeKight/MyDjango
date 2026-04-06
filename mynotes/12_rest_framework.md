
# to install django rest framework 
----------------------------------===================================================
pip install djangorestframework 

- To check: 

pip list
or,
pip show djangorestframework

- 'pip' is used to install any package/anything in python and django projects 
- we can use 'pip' to install: 
  - python libraries(eg: numPy, Panda, Django)
  - django-related libraries (django rest framewrok )
  - any third-party module 

  
# create an API: 
----------------=====================================================================

## step 1: define a function in views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def todo_welcome(request):
    return Response({"detail":"wELCOME"})


## step 2: create a route for it 

from django.urls import path 
from .views import ..., todo_welcome

urlpattens = [
  ...
  path('api/todo/welcome/', todo_api)
]

## run the server 


# create a api with serialier
----------------------------===========================================================

## stepp 1: define a funciton 

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def todo_display(request):
    task = Todo.objects.all()
    serializer = TodoSerializer( task, many=True)
    return Response(serializer.data)

## step 2: define a route 

from django.urls import path 
from .views import ..., todo_diaplay

urlpatterns=[
    ...
    path('api/todo/display/', todo_display),
    
]

## step 3: run the server 



# Note: 
-------==========================================================================
# there is no 'TextField()' in serializer, use 'CharField()' instead 
# both 'TextField()' and 'CharField()' use the same field i.e 'CharField()' . 


# Pros of using rest framework API: 

- Built-in validation (serializers)
- Easy CRUD APIs
- Authentication (JWT, Token)
- Browsable API UI
- Scalable for big projects

# what is JWT ? 