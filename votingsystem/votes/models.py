from django.db import models
from users.models import Account
# Create your models here.


class Question(models.Model):
    question_title = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    voters = models.ManyToManyField(
        Account, related_name="voter", blank=True)

    def __str__(self):
        return self.question_title


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=1024)
    votes = models.IntegerField(default=0)
    # date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.option_text
