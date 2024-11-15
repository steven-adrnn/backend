# api/models.py

from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

class Quiz(models.Model):
    question = models.CharField(max_length=255)
    options = models.JSONField()  # Menyimpan opsi sebagai JSON
    correct_answer = models.CharField(max_length=255)
    
class QuizProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_question_index = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Progress: {self.current_question_index}, Score: {self.score}"