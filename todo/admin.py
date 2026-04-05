from django.contrib import admin

from .models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'priority']
    list_editable= ['status']
    list_per_page = 10
    list_filter = ['status', 'priority']
    search_fields = ('title', 'priority')  # both list or tuple can be used 

# or, 
# admin.site.register(Todo, TodoAdmin)