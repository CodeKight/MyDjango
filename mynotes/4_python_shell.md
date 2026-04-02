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

# all() → “Give me EVERYTHING”
        - Returns ALL records from the table.

        ✔ Example use:
            1. Show all tasks in UI
            2. Admin dashboard listing
            3. Debugging / checking DB data
# filter() → “Give me MATCHING rows”
        * Use filter() when:
        - Field is not unique
        - Multiple results are possible
        - You want conditional data

        ✔ Example use:
            1. Get all completed tasks
            2. Get all tasks of a user
            3. Search functionality
# get() → “Give me EXACT ONE row or crash”
        * Use get() when:
        - Field is PRIMARY KEY (id)
        - Field has unique=True
        - You are 100% sure only one record exists

        - get() is NOT for searching
        - get() is for targeting ONE exact row
        - get() = "I know exactly which record I want"

        ✔ Use cases of get():
        🔹 1. Get by ID
                Fetch a specific record using primary key
                👉 Used when user selects a particular item

        🔹 2. Detail Page / API
                Return data of one item (e.g., /todos/1)
                👉 Used in single-item views or APIs
                
        🔹 3. Update Record
                Get one object, modify it, then save
                👉 Used for editing specific data

        🔹 4. Delete Record
                Get one object, then delete it
                👉 Used when deleting a specific item

        🔹 5. Get using Unique Field
                Fetch using fields with unique=True (like email)
                👉 Used in login or user-specific queries

# all() and filter(): returns query set
- They return a QuerySet (collection of objects)

- 👉 So Django doesn’t know:
- Which object's title??
- That's why we cannot do Todo.objects.filter(status=True).title 

# get(): returns model objects
- It returns a single model object (instance of Todo)
- We can do Todo.objects.get(id=1).title 





### read all data 
Todo.objects.all()

- output: queryset of objects
    <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>, <Todo: Todo object (8)>, <Todo: Todo object (9)>, <Todo: Todo object (10)>, <Todo: Todo object (11)>, <Todo: Todo object (12)>, <Todo: Todo object (13)>]>

### read all data with values 
Todo.objects.all().values()

- output: queryset of dictionanry
    <QuerySet [{'id': 1, 'title': 'first', 'description': 'this is first', 'status': False, 'priority': 'imp'}, {'id': 2, 'title': 'second', 'description': 'this is second', 'status': False, 'priority': 'imp'}, {'id': 3, 'title': 'third', 'description': 'this is third', 'status': True, 'priority': 'very imp'}, {'id': 4, 'title': 'fourth', 'description': 'this is fourth', 'status': False, 'priority': 'very very imp'}, {'id': 5, 'title': 'fifth', 'description': 'this is fifth', 'status': False, 'priority': ' imp'}, {'id': 6, 'title': 'first', 'description': 'this is first', 'status': False, 'priority': ''}, {'id': 7, 'title': 'first', 'description': 'this is first', 'status': False, 'priority': ''}, {'id': 8, 'title': 'first', 'description': '', 'status': False, 'priority': ''}, {'id': 9, 'title': 'nine', 'description': '', 'status': False, 'priority': ''}, {'id': 10, 'title': 'ten', 'description': '', 'status': False, 'priority': ''}, {'id': 11, 'title': 'eleven', 'description': '', 'status': False, 'priority': ''}, {'id': 12, 'title': 'eleven', 'description': '', 'status': False, 'priority': ''}, {'id': 13, 'title': 'eleven', 'description': '', 'status': True, 'priority': ''}]>


### read single data 
Todo.objects.get(id=1)
- output: model object(instance of model Todo)
    <Todo: Todo object (1)>

* Note: get() = get is used to return only one object, if it return multiple object then it shows error 


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
a = Todo.objects.get(id=1)
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
    <QuerySet [{'id': 2, 'title': 'second', 'description': 'this is second', 'status': True, 'priority': 'imp'}, {'id': 3, 'title': 'third', 'description': 'this is third', 'status': True, 'priority': 'very imp'}, {'id': 13, 'title': 'eleven', 'description': '', 'status': True, 'priority': ''}]>

Todo.objects.filter(status=True).title         # error, cannot do this 
- output: 
    ttributeError: 'QuerySet' object has no attribute 'title'




# NOTE: how to access queryset methods --> by using for loop 

## Example 1: Basic QuerySet loop
tasks = Todo.objects.all()

        for t in tasks:
            print(t.title)
            print(t.status)


        - here: 
            - tasks → QuerySet (collection of rows)
            - t → one model object (Todo instance) at a time

        so you can use:
            - t.title
            - t.status

## Example 2: With filter
tasks = Todo.objects.filter(status=True)

        for t in tasks:
            print(t.id, t.title)

## Example 3: Using values() (IMPORTANT DIFFERENCE)
tasks = Todo.objects.values()

        for t in tasks:
            print(t["title"])

### Can also do: 
Todo.objects.values("title").count()


🧠 Difference here:
# Query type	      Inside loop item     	Access style
all() / filter()	    Model object	      t.title
values()	               dict	              t["title"]



# IMP: 

## 1. QuerySet Methods + Return Types

🔹 These return: QuerySet OR other simple types
        all()              → QuerySet
        filter()           → QuerySet
        exclude()          → QuerySet
        order_by()         → QuerySet
        reverse()          → QuerySet

        values()           → QuerySet (of dicts)
        values_list()      → QuerySet (of tuples)

        distinct()         → QuerySet
        annotate()         → QuerySet

        select_related()   → QuerySet
        prefetch_related() → QuerySet


🔹 Special QuerySet methods (with different return types)
        get()        → Model Object
        first()      → Model Object / None
        last()       → Model Object / None
        latest()     → Model Object
        earliest()   → Model Object
        count()      → int     
                    👉count() works on ANY QuerySet
                        ✅QuerySet of objects
                        ✅QuerySet of dictionaries (values())
                        ✅QuerySet of tuples (values_list())
                        ❌Doesn't work on single object like: Todo.objects.get(id=1).count

        exists()     → bool
        aggregate()  → dict
        update()     → int (rows affected)
        delete()     → tuple



## 2. Model Object Methods + Return Types (work on SINGLE row)

- These work on one object like:
    todo = Todo.objects.get(id=1)

🔹 Object methods:
        save()              → None
        delete()            → tuple
        refresh_from_db()   → None
        full_clean()        → None


🔹 Object attributes (not methods but important):
        todo.title
        todo.status
        todo.id
