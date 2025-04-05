from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Question(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ('create_at',)

    def __str__(self):
        return f"Question: {self.text}"



class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)