
# what is Model-View-Template (MVT) ? 
 - Model : database tables, and data inside the database  
 - Views : showing the tables in the browser 
 - Templete : html file/page that is redendered on the browser

 - When a user type any url in the browser then it comes to the url of the project then it goes to the model and send the data from the table to the browser/user 
 - When templete is also included then it grabs the data from the database and populate it in the template then send to the browser. 


# how to use MVT ? 

## step 1: first create models
- skip for now 

## step 2: create views 

from django.http import HttpResponse 

def first(request):  # This is function based views. 
    return HttpResponse("Hello World")

## step 3: create url
from django.urls import path
from .views import first

urlpatterns = [
    path('first/', first)
]

## step 4: add app urls to the project urls 
from django.contrib import admin
from django.urls import path, include  # <-- import 'include' here 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls'))  # <-- add this here # put 'todo.urls' inside quote 
]

#Note: why quote is needed ? because django accepts app path as a string not as a python variable 

## step 5: run the server
- there will be 'Hello World' on the screen. 







# Q. Why need to migrate before creation of models? ----------------------------

❓ Why is Django asking for migrations even if you didn’t create models?

👉 Because Django already comes with built-in apps that HAVE models.

These default apps are:

    admin
    auth
    contenttypes
    sessions

All of them contain pre-defined models like:

    User (login system)
    Permissions
    Session data
    Admin logs

So even if you didn’t create any models, Django still needs to create database tables for these.


❓ What does this message mean?
    You have 18 unapplied migration(s)

👉 It means:

    Django already has migration files ready
    But they are not yet applied to your database


✅ Solution (Do this once)

    Run:
        python manage.py migrate

✔ This will:

    Create tables in your database
    Enable admin login system
    Enable sessions, authentication, etc.


❓ Is it necessary?

    👉 YES, if you want to:

        Use /admin
        Use login/logout system
        Use Django properly


⚠️ Important Note

    This is a one-time setup for a new project.

    After running migrate, you won’t see this warning again (unless new migrations are added).
