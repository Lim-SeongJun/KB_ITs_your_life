from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField() #무제한 길이
    created_at = models.DateTimeField(auto_now_add=True)