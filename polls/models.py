import datetime

from django.contrib import admin
from django.utils import timezone
from django.db import models

# Create your models here.

class Question(models.Model):
    # 字符型
    question_text = models.CharField(max_length=200)
    # 日期型
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='published recently?',
    )
    def was_published_recently(self):
        """
        pub_date:创建日期

        :return:
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    # 主键关联外键
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 整型
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text