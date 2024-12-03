from django.db import models
from django.contrib.auth.models import User


class Employees(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null= True,blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=65)
    address = models.TextField()
    phone = models.IntegerField()
    
    
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    choices = models.JSONField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class UserPerformance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_attempted = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    score = models.FloatField(default=0)

    def update_score(self):
        if self.total_attempted > 0:
            self.score = round(((self.correct_answers / self.total_attempted) * 100), 2)
            self.save()



