from django.core.management.base import BaseCommand
from omi.api.models import Question

# Default sample MCQs
SAMPLE_QUESTIONS = [
    {
        "text": "Which HTTP method is idempotent?",
        "option_a": "POST",
        "option_b": "PUT",
        "option_c": "PATCH",
        "option_d": "CONNECT",
        "correct_option": "B",
    },
    {
        "text": "Which React hook is used to manage state in a functional component?",
        "option_a": "useMemo",
        "option_b": "useEffect",
        "option_c": "useState",
        "option_d": "useRef",
        "correct_option": "C",
    },
    {
        "text": "In SQL, which clause filters rows after grouping?",
        "option_a": "WHERE",
        "option_b": "HAVING",
        "option_c": "GROUP BY",
        "option_d": "ORDER BY",
        "correct_option": "B",
    },
    {
        "text": "What does JWT stand for?",
        "option_a": "Java Web Token",
        "option_b": "JSON Web Token",
        "option_c": "JavaScript Web Token",
        "option_d": "Joined Web Token",
        "correct_option": "B",
    },
    {
        "text": "Which HTTP status code indicates 'Unauthorized'?",
        "option_a": "403",
        "option_b": "500",
        "option_c": "401",
        "option_d": "422",
        "correct_option": "C",
    },
    {
        "text": "Which database is a NoSQL database?",
        "option_a": "MySQL",
        "option_b": "PostgreSQL",
        "option_c": "MongoDB",
        "option_d": "SQLite",
        "correct_option": "C",
    },
    {
        "text": "Which Python web framework is most commonly used for REST APIs?",
        "option_a": "Flask",
        "option_b": "FastAPI",
        "option_c": "Django REST Framework",
        "option_d": "Pyramid",
        "correct_option": "C",
    },
    {
        "text": "Which React hook is used to perform side effects?",
        "option_a": "useEffect",
        "option_b": "useState",
        "option_c": "useCallback",
        "option_d": "useReducer",
        "correct_option": "A",
    },
    {
        "text": "Which SQL command is used to remove all rows from a table but keep the structure?",
        "option_a": "DROP",
        "option_b": "DELETE",
        "option_c": "TRUNCATE",
        "option_d": "REMOVE",
        "correct_option": "C",
    },
    {
        "text": "Which JavaScript method converts JSON text to a JavaScript object?",
        "option_a": "JSON.parse()",
        "option_b": "JSON.stringify()",
        "option_c": "JSON.decode()",
        "option_d": "JSON.toObject()",
        "correct_option": "A",
    }
]


class Command(BaseCommand):
    help = "Seed the database with default MCQ questions"

    def handle(self, *args, **kwargs):
        """
        Usage:
            python manage.py seed_questions
        """
        # Check if there are existing questions
        if Question.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    f"Skipped! There are already {Question.objects.count()} questions in the database."
                )
            )
            return

        # Create all sample questions
        Question.objects.bulk_create([Question(**q) for q in SAMPLE_QUESTIONS])

        # Success message
        self.stdout.write(
            self.style.SUCCESS(f"Successfully seeded {len(SAMPLE_QUESTIONS)} questions.")
        )
