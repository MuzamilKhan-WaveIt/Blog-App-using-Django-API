from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Model(models.Model):
    id  = models.UUIDField(primary_key = True, editable = False, unique = True, default = uuid.uuid4)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title + " | " + self.author.username
