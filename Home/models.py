from django.db import models
from django.contrib.auth.models import User
 
class USER(models.Model):
    username = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fields = models.TextField()

    def __str__(self):
        return self.user.username
