# step 1: create the python shell 
python manage.py shell 

- this python shell is same as opening the python app and using that shell 
- this shell is project specific and that was global 


# step 2: performing CRUD operation using shell 

## step 1: import the model 
from todo.models import Todo 

## step 2: get all the data from the table/model 
Todo.objects.all()   # all the data in the models are displayed 

- sytax: 
    model_name.objects.all()

- result: 
    <QuerySet []>   # <-- it means the table is empty 

## step 3: create (C) data in the table 
model_name.objects.create(field1="value1", field2="value2", field3="value3", ... )

Todo.objects.create(title="first", description = "this is first", status = False, priority = "imp")

- output:
    <Todo: Todo object (1)>   # 1 row insesrted or one object created, whose id is 1 

## step 4: insert multiple rows
- also works if all column are not mentioned 
    - eg: 
        Todo.objects.create(title="first")       # only 'title' was given, not all the columns 
    - output: 
        <Todo: Todo object (8)>    # meaning an object is created, means value inserted with an id 8

- also works if column are given radomly, not serially
    - eg: 
        Todo.objects.create(title="eleven", status=True)       # columns are not given serially 
    - output: 
        <Todo: Todo object (13)>


## step 5: read (R) data 

### read all data 
Todo.objects.all()

- output: 
    <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>, <Todo: Todo object (8)>, <Todo: Todo object (9)>, <Todo: Todo object (10)>, <Todo: Todo object (11)>, <Todo: Todo object (12)>, <Todo: Todo object (13)>]>

### read all data with values 
Todo.objects.all().values()

- output: 
    <QuerySet [{'id': 1, 'title': 'first', 'description': 'this is first', 'status': False, 'priority': 'imp'}, {'id': 2, 'title': 'second', 'description': 'this is second', 'status': False, 'priority': 'imp'}, {'id': 3, 'title': 'third', 'description': 'this is third', 'status': True, 'priority': 'very imp'}, {'id': 4, 'title': 'fourth', 'description': 'this is fourth', 'status': False, 'priority': 'very very imp'}, {'id': 5, 'title': 'fifth', 'description': 'this is fifth', 'status': False, 'priority': ' imp'}, {'id': 6, 'title': 'first', 'description': 'this is first', 'status': False, 'priority': ''}, {'id': 7, 'title': 'first', 'description': 'this is first', 'status': False, 'priority': ''}, {'id': 8, 'title': 'first', 'description': '', 'status': False, 'priority': ''}, {'id': 9, 'title': 'nine', 'description': '', 'status': False, 'priority': ''}, {'id': 10, 'title': 'ten', 'description': '', 'status': False, 'priority': ''}, {'id': 11, 'title': 'eleven', 'description': '', 'status': False, 'priority': ''}, {'id': 12, 'title': 'eleven', 'description': '', 'status': False, 'priority': ''}, {'id': 13, 'title': 'eleven', 'description': '', 'status': True, 'priority': ''}]>


### read single data 
Todo.objects.get(id=1)
- output: <Todo: Todo object (1)>


### read single data with values
Todo.objects.get(id=1).title
- output: 'first'

or,

a = Todo.objects.get(id=1)
a.title
   - output: 'first'

a.description
   - output: 'this is first'

a.status
   - output: False


## step 5: update (U) data
a.status
- output: False 

a.status = True
a.status
- output: True

a.save()    # this will save the updated data to the database 

## step 6: delete (D) data
a.delete()
- output: 
    (1, {'todo.Todo': 1})


# 3. filter data 
Todo.objects.filter(status=True)
- output: 
    <QuerySet [<Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (13)>]>

Todo.objects.filter(status=True).values()
- output: 
    <QuerySet [<Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (13)>]>

Todo.objects.filter(status=True).title         # error, cannot do this 
- output: 
    ttributeError: 'QuerySet' object has no attribute 'title'
