
# how to edit data of a doto-app ?
---------------------------------================================================================

## step 1: create a route with id  

from django.urls import path 
from .views import ..., todo_edit

urlpatterns=[
    ...
    path('todo/edit/<id>/', todo_edit),
]


## step 2: create the template for edit (todo_edit.html)
- it will contain a form and a alert box same as create 
- but it will fetch the data with id to edit 


{%if error %}
<div class="container">
    <div class="alert alert-danger" role="alert">
        {{error}}
    </div>
</div>
{% endif %}

  
<div class="container ">
    <form method="POST"">
        {% csrf_token %}        
        <div class=" mb-3">
        <label for="exampleInputEmail1" class="form-label"> Title </label>
        <input name="title"  value={{task.title}} type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
</div>

<div class="form-floating mb-3">
    <textarea name="description" class="form-control" placeholder="Leave a comment here"
        id="floatingTextarea"></textarea>
    <label for="floatingTextarea">{{task.description}} </label>
</div>

<button type="submit" class="btn btn-primary">Edit</button>
</form>
</div>

## step 3: put the "name" attributes in inputs to get form data in the views

## step 4: create funciton for edit in views 


def todo_edit(request,id):
    task = Todo.objects.get(id=id)
    context = {
        'task': task 
    }
    if request.method=='POST': 
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title 
        task.description = description 
        task.save()
        return redirect('/todo/')
        
    return render(request, 'todo_edit.html', context) 

- the data will be successfully edited. 



# creating button for edit  
--------------------------===========================================================================

## step 1: go to main todo.html 

## step 2: create a new <th> in the table head and name it 'Action'


 <thead>
    <tr>
        ...
        <th scope="col">Action</th>      
    </tr>
</thead>

## step: add a new <td> for with a button named 'Edit'

 <tbody>
    {%for i in tasks%}
        <tr>
            ...  
            <td> <button class="btn btn-primary">Edit</button> </td>
        </tr>
    {%endfor%}
</tbody>

## step 4: change button into <a> tag

## step 5: put the route path in the 'href' of <a>
- use {{i.id}} to provide the id from the db

    ...  
    <td> <a href="edit/{{i.id}}/" class="btn btn-primary">Edit</a> </td>

- the button is successfully created. 
- add the class 'btn-primary' to give it blue color

- when clicked on buttons, it will call the path of urls 
- urls will call the respective function 
- the function will perforn the edit operation
- then it will redirect to the main page.


# creating button for mark 
-------------------------===================================================================

## step 1: go to main todo.html 

## step 2: add a new <td> for with a button named 'Mark'

 <tbody>
    {%for i in tasks%}
        <tr>
            ...  
            <td> <button class="btn btn-success">Mark</button> </td>
        </tr>
    {%endfor%}
</tbody>

## step 3: change button into <a> tag

## step 4: put the route path in the 'href' of <a>
- use {{i.id}} to provide the id from the db

    ...  
    <td> <a href="edit/{{i.id}}/" class="btn btn-success">Edit</a> </td>

- the button is successfully created. 
- add the class 'btn-success' to give it green color

## step 5: goto urls.py and define the route there 

from django.urls import path 
from .views import ..., todo_mark

urlpatterns=[
    ...
    path('todo/edit/<id>/', todo_mark),
]

## step 6: goto view.py and writ the function for mark there

def todo_mark(request,id):
    task = Todo.objects.get(id=id)
    task.status = True
    task.save()
    return redirect('/todo/')

- the mark button is successfully created 
- when clicked on mark it will change the status
- then it will redirect the main page 


# creating the delete button
---------------------------================================================================

## step 1: go to main todo.html 

## step 2: add a new <td> for with a button named 'Delete'

 <tbody>
    {%for i in tasks%}
        <tr>
            ...  
            <td> <button class="btn btn-danger"> Delete </button> </td>
        </tr>
    {%endfor%}
</tbody>

## step 3: change button into <a> tag

## step 4: put the route path in the 'href' of <a>
- use {{i.id}} to provide the id from the db

    ...  
    <td> <a href="delete/{{i.id}}/" class="btn btn-danger">Delete</a> </td>

- the button is successfully created. 
- add the class 'btn-danger' to give it red color

## step 5: goto urls.py and define the route there 


from django.urls import path 
from .views import ..., todo_delete

urlpatterns=[
    ...
    path('todo/edit/<id>/', todo_delete),
]


## step 6: goto view.py and write the delete function

def todo_delete(request,id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('/todo/')

- the delete button is successfully created 
- when clicked on delete it will delete the data(the whole row)
- then it will redirect the main page
