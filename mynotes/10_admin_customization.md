
# to open the admin panel 
------------------------=========================================================

## step 1: create a superuser
py manage.py createsuperuser

## step 2: run the server and login 
- go to the 'admin/' route 
- enter the username and password
- login to the admin panel 
- explore the admin panel 

# register "Todo" model in admin panel
-------------------------------------=============================================

## step 1: goto 'admin.py' of the app(i.e todo) and register the 'Todo' 

from django.contrib import admin 
form .models import Todo 

admin.site.register(Toto)

- now the 'Todo' model will be shown in the admin panel 

### add this in the model class to show model field as a string 

def __str__(self):
        return self.title


# to do admin customization
--------------------------=========================================================

from django.contrib import admin 

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'priority']
    list_per_page = 10
    list_filter = ['status', 'priority']
    search_fields = ("title")  # both list or tuple can be used 
    list_editable= ('status')

# or, 
# admin.site.register(Todo, TodoAdmin)

