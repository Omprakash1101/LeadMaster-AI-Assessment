from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Exam, Submission


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("username", "password")
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "text", "option_a", "option_b", "option_c", "option_d")


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ("id", "created_at", "duration_seconds")


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("id", "exam", "submitted_at", "answers_json", "score")