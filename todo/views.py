from django.shortcuts import render
from django.http import HttpResponse

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
        "first_line": "welcome to the homepage, this is dynamic rendering",
        "second_line": "this is homepage rendering from function",
        "people": people
    }
    
    return render(request, 'home.html', context)


# Note: 
# {{ i.name }} -  dynamic 
# Underage     -  tatic text 


# 🔥 Simple Rule
# {{ }} → for variables / dynamic values
# {% %} → for logic (if, for, etc.)
# Plain text → automatically displayed


# A block is determined only by template tags, not by:

# line breaks ❌
# indentation ❌
# spacing ❌

# A block starts at a tag and continues until the next relevant tag











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


