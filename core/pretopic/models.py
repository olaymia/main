from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Topic(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(BaseModel):
    MCQ = 'Single Choice Question'
    MULTIPLE_SELECT = 'Multiple Select Question'
    QUESTION_TYPES = [
        (MCQ, 'Single Choice Question'),
        (MULTIPLE_SELECT, 'Multiple Select Question'),
    ]

    text = models.TextField()
    topic = models.ForeignKey(Topic, related_name='topic_questions', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    marks = models.IntegerField(default=1)
    time_limit = models.IntegerField(default=90)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text




