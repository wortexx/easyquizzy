from django.db import models

# Create your models here.
class Quiz(models.Model):
    topic = models.CharField(max_length = 400)
    subject = models.CharField(max_length = 200)

    def __str__(self):
        return self.topic + ' (' + self.subject + ')'

    class Meta:
        verbose_name_plural = "quizes"      

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    explanation_text = models.CharField(max_length=1000)
    cost = models.IntegerField(default=5)

    @property
    def multichoice(self):
        'Returns whether it is a multichoice question'
        return self.choice_set.filter(correct = True).count() > 1
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    