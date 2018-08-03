from django.db import models

# Create your models here.
class Question(models.Model): #index.html페이지에서 질문 저장할 곳
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200) #답변 저장
    votes = models.IntegerField(default=0)#투표카운트

    def __str__(self):
        return self.choice_text