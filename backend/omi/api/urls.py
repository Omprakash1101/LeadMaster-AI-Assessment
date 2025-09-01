from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    start_exam,
    submit_exam,
    exam_result,
    health
)

urlpatterns = [
    # -------------------------
    # Authentication Endpoints
    # -------------------------
    path("auth/register/", RegisterView.as_view(), name="register"),         # POST → Register a new user
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),        # POST → Get JWT access & refresh tokens
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # POST → Refresh JWT token

    # -------------------------
    # Exam Endpoints
    # -------------------------
    path("exam/start/", start_exam, name="start_exam"),                      # POST → Start an exam & fetch random questions
    path("exam/<int:exam_id>/submit/", submit_exam, name="submit_exam"),     # POST → Submit exam answers & calculate score
    path("exam/<int:exam_id>/result/", exam_result, name="exam_result"),     # GET  → Get exam results

    # -------------------------
    # Health Check Endpoint
    # -------------------------
    path("health/", health, name="health_check"),                           # GET → API health check
]
