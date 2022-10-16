from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)