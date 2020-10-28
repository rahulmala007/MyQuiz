from django.db import models
from quiz.models import quiz

# Create your models here.

class MCQ(models.Model):
    quiz=models.ForeignKey("quiz.quiz",on_delete=models.CASCADE)
    image=models.ImageField(upload_to='MCQ/',null=True,blank=True)
    description=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer_value=models.IntegerField()

    def is_MCQ(self):
        return True

class OpenText(models.Model):
    quiz=models.ForeignKey("quiz.quiz",on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Text/',null=True,blank=True)
    description=models.CharField(max_length=100)
    answer_content=models.CharField(max_length=100)

    def is_MCQ(self):
        return False


class MCQAnswer(models.Model):
    question=models.ForeignKey(MCQ,on_delete=models.CASCADE)
    answer_value=models.IntegerField()
    isCorrect=models.BooleanField()

class OpenTextAnswer(models.Model):
    question=models.ForeignKey(OpenText,on_delete=models.CASCADE)
    answer_content=models.CharField(max_length=100)
    isCorrect=models.BooleanField()