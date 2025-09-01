import random
from typing import List
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import (
    RegisterSerializer,
    QuestionSerializer,
    ExamSerializer,
    SubmissionSerializer
)
from .models import Question, Exam, Submission


# --------------------------
#  USER REGISTRATION
# --------------------------
class RegisterView(generics.CreateAPIView):
    """
    Endpoint: POST /api/auth/register/
    Body: { "username": "...", "password": "..." }
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# --------------------------
#  START EXAM
# --------------------------
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def start_exam(request):
    """
    Endpoint: POST /api/exam/start/
    Body: { "count": 5 }
    Returns: { "exam": {...}, "questions": [...] }
    """
    count = int(request.data.get("count", 10))
    if count < 1:
        count = 1

    # Get all available question IDs
    ids: List[int] = list(Question.objects.values_list("id", flat=True))
    if not ids:
        return Response({"detail": "No questions available"}, status=400)

    if count > len(ids):
        count = len(ids)

    # Randomly select unique question IDs
    selected = random.sample(ids, count)

    # Create an exam object and freeze selected question IDs
    exam = Exam.objects.create(
        user=request.user,
        question_ids_csv=",".join(map(str, selected))
    )

    # Fetch the selected questions and serialize them
    questions = Question.objects.filter(id__in=selected)
    ser = QuestionSerializer(questions, many=True)

    return Response({
        "exam": ExamSerializer(exam).data,
        "questions": ser.data
    })


# --------------------------
#  SUBMIT EXAM
# --------------------------
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def submit_exam(request, exam_id: int):
    """
    Endpoint: POST /api/exam/<exam_id>/submit/
    Body: { "answers": { "1": "A", "2": "C" } }
    Returns: { "exam": {...}, "score": 3, "answers_json": {...} }
    """
    exam = get_object_or_404(Exam, pk=exam_id)

    # Ensure the exam belongs to the requesting user
    if exam.user != request.user:
        return Response({"detail": "Forbidden"}, status=403)

    # Prevent multiple submissions
    if hasattr(exam, "submission"):
        return Response({
            "detail": "Exam already submitted",
            "score": exam.submission.score
        }, status=400)

    # Extract answers from request
    answers = request.data.get("answers", {})

    # Retrieve frozen question IDs from exam object
    try:
        frozen_ids = [int(x) for x in exam.question_ids_csv.split(",") if x]
    except ValueError:
        frozen_ids = []

    questions = Question.objects.filter(id__in=frozen_ids)

    # Calculate score
    score = 0
    for q in questions:
        selected = str(answers.get(str(q.id)) or answers.get(q.id))
        if selected and selected.upper() == q.correct_option:
            score += 1

    # Create submission record
    submission = Submission.objects.create(
        exam=exam,
        answers_json=answers,
        score=score
    )

    return Response(SubmissionSerializer(submission).data)


# --------------------------
#  GET EXAM RESULT
# --------------------------
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def exam_result(request, exam_id: int):
    """
    Endpoint: GET /api/exam/<exam_id>/result/
    Returns: { "score": 3, "answers_json": {...}, "submitted_at": "..." }
    """
    exam = get_object_or_404(Exam, pk=exam_id)

    # Ensure exam belongs to requesting user
    if exam.user != request.user:
        return Response({"detail": "Forbidden"}, status=403)

    # Check if the exam has been submitted
    if not hasattr(exam, "submission"):
        return Response({"detail": "Exam not submitted yet"}, status=400)

    return Response(SubmissionSerializer(exam.submission).data)


# --------------------------
#  HEALTH CHECK
# --------------------------
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def health(request):
    """
    Endpoint: GET /api/health/
    Returns: {"status": "ok"}
    """
    return Response({"status": "ok"})
