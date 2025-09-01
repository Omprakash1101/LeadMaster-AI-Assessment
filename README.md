# 🎓 LeadMasters AI – Online Exam System

An **AI-driven online exam platform** built with **Django REST Framework** (backend) and **React** (frontend).  
It provides secure authentication, randomized question selection, automated scoring, and result management.

---

## **🚀 Features**
- 🔐 **JWT Authentication** (Register, Login, Refresh)
- 📝 Start an exam with random questions
- 🧠 Automatic scoring on submission
- 📊 View exam results instantly
- 🛠 Seeder command to populate questions
- 🌐 Fully API-driven → Easily testable via **Postman**

---

## **🛠️ Tech Stack**
- **Backend:** Django, Django REST Framework, SimpleJWT
- **Frontend:** React (Vite), Axios, React Router
- **Database:** SQLite (default) / PostgreSQL (optional)
- **API Testing:** Postman

---

## **📂 Project Structure**

LeadMasters-AI-ASSESSMENT/
├─ backend/
│ ├─ manage.py
│ ├─ requirements.txt
│ ├─ .env.example
│ ├─ Dockerfile
│ ├─ docker-compose.yml
│ └─ omi/
│ ├─ __init__.py
│ ├─ settings.py
│ ├─ urls.py
│ ├─ wsgi.py
│ └─ api/
│ ├─ __init__.py
│ ├─ apps.py
│ ├─ models.py
│ ├─ serializers.py
│ ├─ permissions.py
│ ├─ views.py
│ ├─ urls.py
│ ├─ admin.py
│ └─ management/
│ └─ commands/
│ └─ seed_questions.py
│
└─ frontend/
├─ index.html
├─ package.json
├─ vite.config.js
└─ src/
├─ main.jsx
├─ App.jsx
├─ api.js
├─ auth.jsx
├─ components/
│ ├─ Navbar.jsx
│ └─ Timer.jsx
└─ pages/
├─ Register.jsx
├─ Login.jsx
├─ StartExam.jsx
├─ Exam.jsx
└─ Result.jsx

## **⚡ Backend Setup**
```bash
git clone https://github.com/Omprakash1101/LeadMaster-AI-Assessment.git
cd LeadMaster-AI-Assessment/backend
python -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py seed_questions
python manage.py runserver
```
## **⚡ frontend Setup**
```bash
cd ../frontend
npm install
npm run dev
```

## **Sample Output**
![Screenshot](https://github.com/Omprakash1101/LeadMaster-AI-Assessment/img/1.png)

## **📞 Support**

For any queries or assistance, feel free to reach out:

**Author:** Omprakash G<br>
**Email:** omprakashgopi2k05@gmail.com<br>
**GitHub:** @Omprakash1101