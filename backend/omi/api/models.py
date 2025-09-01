from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    CORRECT_CHOICES = [(ch, ch) for ch in ["A", "B", "C", "D"]]
    correct_option = models.CharField(max_length=1, choices=CORRECT_CHOICES)


    def __str__(self):
        return self.text[:50]


class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    duration_seconds = models.IntegerField(default=1800) # 30 min default
    # Keep a frozen question set for fairness
    question_ids_csv = models.TextField() # comma-separated IDs


class Submission(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    answers_json = models.JSONField() # {question_id: "A"}
    score = models.IntegerField()