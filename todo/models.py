from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=40, default="imp")
    
    def __str__(self):
        return self.title

    
    
   
    