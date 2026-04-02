
# how to create new data in a todo-app

## step 1: create a route for 'task_create'

from django.urls import path 
from .views import ..., todo_create

urlpatterns=[
    ...
    path('todo/edit/<id>/', todo_create),
]

## step 2: create a template with a form
* add csrf toekn inside the form to create data 

<div class="container ">
    <form method="POST"">
        {% csrf_token %}     # 👈 csrf token added here
        <div class=" mb-3">
        <label for="exampleInputEmail1" class="form-label"> Title </label>
        <input name="title" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
</div>

<div class="form-floating mb-3">
    <textarea name="description" class="form-control" placeholder="Leave a comment here"
        id="floatingTextarea"></textarea>
    <label for="floatingTextarea">Description </label>
</div>

<button type="submit" class="btn btn-primary">Create</button>
</form>
</div>

## step 3: put name attribut in the input fields eg: name = "title", name = "description"

## step 4: define function for CREATE OPERATION in views. 

def todo_create(request):
    if request.method=='POST': 
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title=='' or description == '':
      
            context = {
                "error": "Both fields are required",  
            }
            return render(request, 'todo_create.html',context)
        Todo.objects.create(title=title, description= description)
        return redirect('/todo/')
  
    return render(request,'todo_create.html')    

## step 5: for error , create an aleart box and sent the error with if statement in it

{%if error %}
<div class="container">
    <div class="alert alert-danger" role="alert">
        {{error}}   # ⬅️ error sent here 
    </div>
    

</div>
{% endif %}