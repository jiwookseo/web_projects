from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shout(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title[:20]} : {self.content[:20]}"