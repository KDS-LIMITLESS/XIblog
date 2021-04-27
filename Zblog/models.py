from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"Comment by {self.username} "

