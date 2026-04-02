# what is templates ? 
- it is the html page that can be render inside the django environment 
- it is used to develop the full stack app 
- it is used to make the dynamic webpages 


# how to use templates in djago ? 

## step 1: create 'templates' folder inside the current location 

## step 2: add this folder in settings.py in 'TEMPLATES' 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],  # ⬅️ ADD here, with quote  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

- Note: if you remove 'BASE_DIR' from here, then also there won't be any error 

## step 3: create a html file inside it eg: 'home.html' 

## step 4: render html page using views ( in view.py )

from django.shortcuts import render 

def home(request):
  return render(request, 'home.html')

## step 5: run the server 
- the html page will be rendered on the browser 



# sending dynamic data on the webpage

## step 1: in views.py : 

def home(request):
    context = {                                                  # ⬅️ this was added here 
        "first_line": "welcome to the page, this dynamic ",
        "second_line": "this is homepage rendering from function"
    }
    return render(request, 'home.html', context)   # ⬅️ context was passed as argumment in 'render'

## step 2: in home.html: 

<body>
    <h1> {{first_line}} </h1>
    <p> {{second_line}} </p>
</body>

## step 3: run the server 



# creating dynamic table using bootstrap 
## in views.py: 

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


## in home.html:


### ⬇️add link in header and script just before body

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
    crossorigin="anonymous"></script>



### create table using foreach loop. 

# forloop.counter  - to show id in increasing order.  

        <table class="table   table-striped">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col">Age</th>
                    <th scope="col">Salary</th>
                    <th scope="col">Address</th>
                </tr>
            </thead>
            <tbody>
                 {%for i in people%} 
                 <tr>
                    <th scope="row"> {{forloop.counter}} </th> 
                    <td> {{i.name}} </td>
                    <td> {{i.age}}</td>
                    <td> {{i.salary}} </td>
                    <td> {{i.address}} </td>
                </tr>
                {%endfor%}
            </tbody>
        </table>

# you can also put conditions using if-else statement.
        <table class="table   table-striped">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col">Age</th>
                    <th scope="col">Salary</th>
                    <th scope="col">Address</th>
                </tr>
            </thead>
            <tbody>

                {%for i in people%}  
                  
                 <tr>
                    <th scope="row"> {{forloop.counter}} </th> 
                    <td> {{i.name}} </td>

                    <td> 
                        {% if i.age < 18%}   #🔺 if condition is put here 
                            Underage 
                        {%elif i.age >= 18 and i.age < 50 %} 
                            Adult
                        {%else%} 
                            Old 
                        {%endif%}

                        ({{i.age}})
                    </td>
                    <td> {{i.salary}} </td>
                    <td> {{i.address}} </td>
                </tr>
                {%endfor%}
            </tbody>
        </table>

---------------------------------------------------------------------------------


# Note: 
# {{ i.name }} -  dynamic 
# Underage     -  static text 


# 🔥 Simple Rule
# {{ }} → for variables / dynamic values
# {% %} → for logic (if, for, etc.)
# Plain text → automatically displayed


# A block is determined only by template tags, not by:

# line breaks ❌
# indentation ❌
# spacing ❌

# A block starts at a tag and continues until the next relevant tag