# step 1: design the database ( db.txt file created )
Table : Todolist
- title        - char
- description  - text 
- time         - date/time 
- priority     - int/char
- status (completed/incompleted)      - boolean 

# step 2: model was created in models.py

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=False)
    priority = models.TextField()

# step 3: make migrations of the models
py manage.py makemigrations             # <-- this will create the migration files 

# step 4: migrate 
py manage.py migrate   # <-- this will reflect the model/table in the database 


    
