from django.contrib import admin
from .models import Question, Exam, Submission


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "correct_option")
    search_fields = ("text",)
    list_filter = ("correct_option",)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "duration_seconds")
    list_filter = ("created_at",)
    search_fields = ("user__username",)
    ordering = ("-created_at",)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "exam", "score", "submitted_at")
    list_filter = ("submitted_at",)
    search_fields = ("exam__user__username",)
    ordering = ("-submitted_at",)
