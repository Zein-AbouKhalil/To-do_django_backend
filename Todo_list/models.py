from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
