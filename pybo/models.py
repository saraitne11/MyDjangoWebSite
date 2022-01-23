from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete=models.CASCADE -> 계정이 삭제되면 해당 계정과 연결된 Question 데이터 모두 삭제

    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete=models.CASCADE -> 계정이 삭제되면 해당 계정과 연결된 Question 데이터 모두 삭제

    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
