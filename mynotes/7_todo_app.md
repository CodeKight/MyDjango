
# how to create a todo app 

## step 1: view


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


## step 2: in urls
from django.urls import path 

urlpatterns=[
    ... 
    path('todo/', todo),
    ...

]

## step 3: create a template eg: todo.html

## step 4: in todo.html

* put the table in a div and give it a class = "container" to center it 

{% extends "base.html" %}
{%block title %}   {{title}}  {% endblock title%}

{% block body %}


    <h1> To-do app  </h1>
    <p> This is to-do app </p>
    <h3> Total task : {{total}} </h3>
    <h3> Completed task: {{completed}} </h3>
    <h3> Incompleted task: {{incompleted}} </h3>

    <!-- creating dynamic table using bootstrap -->
    <div class="container">
        <table class="table   table-striped" "table-primary" >
            <thead>
                <tr>
                    <th scope="col">S.N</th>
                    <th scope="col">Title</th>
                    <th scope="col">Description</th>
                    <th scope="col">Priority</th>
                    <th scope="col">Status</th>
                </tr>
            </thead>
            <tbody>
                {%for i in tasks%}
                <tr>
                    <th scope="row"> {{forloop.counter}} </th>
                    <td> {{i.title}} </td>
                    <td> {{i.description}} </td>
                    <td> {{i.priority}} </td>
                    <td> {{i.status}} </td>
                </tr>
                {%endfor%}

            </tbody>
        </table>

    </div>


{%endblock body%}

## step 5: run the server 
- the todo table will be created on the browser html page. 