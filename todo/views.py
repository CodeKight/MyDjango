from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.

def home(request):
    people = [
    {"name": "Aarav", "age": 25, "salary": 50000, "address": "Kathmandu"},
    {"name": "Sita", "age": 30, "salary": 60000, "address": "Pokhara"},
    {"name": "Ram", "age": 16, "salary": 55000, "address": "Lalitpur"},
    {"name": "Gita", "age": 35, "salary": 70000, "address": "Bhaktapur"},
    {"name": "Hari", "age": 40, "salary": 80000, "address": "Biratnagar"},
    {"name": "Nita", "age": 17, "salary": 52000, "address": "Butwal"},
    {"name": "Kiran", "age": 32, "salary": 65000, "address": "Dharan"},
    {"name": "Anita", "age": 29, "salary": 58000, "address": "Hetauda"},
    {"name": "Ramesh", "age": 45, "salary": 90000, "address": "Janakpur"},
    {"name": "Sunita", "age": 31, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 60, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 31, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 31, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 50, "salary": 62000, "address": "Nepalgunj"},    # this is dynamic, the more you add the data here the more rows in the table of homepage will be added 
    ]
    
    context ={
        "title":"Home",
        "first_line": "welcome to the homepage, this is dynamic rendering",
        "second_line": "this is homepage rendering from function",
        "people": people
    }
    
    return render(request, 'home.html', context)


def contact(request):
    context = {
        "title": "Contact_extends",
        "first_line": "this is contact",
        "second_line": "this is contact page rendering from contact function",
        
    }
    return render(request, 'contact_extends.html', context)

def home_extends(request):
    
    people = [
    {"name": "Aarav", "age": 25, "salary": 50000, "address": "Kathmandu"},
    {"name": "Sita", "age": 30, "salary": 60000, "address": "Pokhara"},
    {"name": "Ram", "age": 16, "salary": 55000, "address": "Lalitpur"},
    {"name": "Gita", "age": 35, "salary": 70000, "address": "Bhaktapur"},
    {"name": "Hari", "age": 40, "salary": 80000, "address": "Biratnagar"},
    {"name": "Nita", "age": 17, "salary": 52000, "address": "Butwal"},
    {"name": "Kiran", "age": 32, "salary": 65000, "address": "Dharan"},
    {"name": "Anita", "age": 29, "salary": 58000, "address": "Hetauda"},
    {"name": "Ramesh", "age": 45, "salary": 90000, "address": "Janakpur"},
    {"name": "Sunita", "age": 31, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 60, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 31, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 31, "salary": 62000, "address": "Nepalgunj"},
    {"name": "Sunita", "age": 50, "salary": 62000, "address": "Nepalgunj"},    # this is dynamic, the more you add the data here the more rows in the table of homepage will be added 
    ]
    
    context = {
        "title": "Home_extends",
        "first_line": "this is homepage with extends",
        "second_line": "this is homepage rendering from function",
        "people": people
    }
    return render(request, 'home_extends.html', context)


# todo app 

def todo(request):
    tasks = Todo.objects.all()    # getting all the data from the table in a list of dictionary format
    total = tasks.count()
    completed = Todo.objects.filter(status = True).count()
    incompleted = Todo.objects.filter(status = False).count()
    
    context = {
        "title": "To-do app", 
        "tasks": tasks,
        "total": total, 
        "completed": completed,
        "incompleted":incompleted
    }
    return render(request, 'todo.html', context)













# def home(request):
#     context = {
#         "first_line": "welcome to the page, this dynamic ",
#         "second_line": "this is homepage rendering from function"
#     }
#     return render(request, 'home.html', context)














# def first(request):
#     # return HttpResponse("Hello World")
#     return HttpResponse("<h1> Hello world again </h1> ")  # can also sent html element

# def home(request):
#     return HttpResponse("<h2> This is home. </h2>  ")

# def contact_us(request):
#     return HttpResponse("<h3> This is cotact. <h3> ")


