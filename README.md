
# django-quizz-app

# Django Quiz Application

## 🚀 Project Overview
Welcome to the Django-based Quiz Application! This app is designed to provide a fun and interactive quiz experience with user registration, login, and real-time feedback. It was developed as part of a Python internship assignment.

## ✨ Features
### 🔐 User Authentication
- Secure registration and login system with Django’s built-in authentication system.

### 🎮 Dynamic Quizzes
- Questions are dynamically loaded during each quiz session.
- Instant feedback on whether your answer is correct or incorrect.

### 📊 Result Tracking
- Track your quiz performance, including correct and incorrect answers.

### 🏠 Responsive Dashboard
- A clean and intuitive dashboard to start new quizzes or review results.

### 🔒 Session Management
- Secure quiz session management, with no reliance on JavaScript.

## 🛠️ Technologies Used
- Backend: Django (Python)
- Frontend: HTML, CSS (No JavaScript)
- Database: SQLite
- Hosting: Django Development Server (local setup)
  
### Prerequisites
- Python 3.x installed.
- Basic understanding of Python and Django.  

## 🏁 Setup Instructions
To get started, follow the steps below:

### Clone the Repository
```bash
git clone https://github.com/sagunadk7/quizz_app
cd quizz_app
```

### Create a Virtual Environment
#### For Linux/Mac:
```bash
python -m venv env
source env/bin/activate
```
#### For Windows:
```bash
python -m venv env
env\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### Run the Development Server
```bash
python manage.py runserver
```

### Access the Application
Go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🗂️ Folder Structure
- `quiz_app/`: Main Django app (models, views, templates).
- `templates/`: HTML files for the interface.
- `db.sqlite3`: SQLite database containing user and quiz data.
- `manage.py`: Django project management script.
- `README.md`: Project documentation file containing setup steps, project overview, and instructions.

## 🎮 Usage
### 🔑 Registration/Log In:
- Register a new user or log in to access the quiz.

### 💡 Take the Quiz:
- Answer the questions, receive immediate feedback, and see if you’re correct or not!

### 📈 View Results:
- See your overall performance after completing the quiz.

### 🖥️ Dashboard:
- Return to the dashboard to retake the quiz or log out.

### ⚠️ Note for SuperUser: Adding Questions and Choices from the Admin Panel
To manage quiz questions and choices, follow these steps:

1. **Create SuperUser (if not done already)**:
   ```bash
   python manage.py createsuperuser
   ```

2. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

3. **Go to the Admin Panel**:
   Open your browser and visit:  
   ```
   http://127.0.0.1:8000/admin/
   ```

4. **🔑Log in with SuperUser Credentials**.

5. **🔍Navigate to the Questions Section**:
   Click on the `Questions` model.

6. **🎲Add a New Question**:
   Click the **Add Question** button, fill in the details, and click **Save**.

7. **💬Add Choices for the Question**:
   After saving the question, click the **Add Choice** button to add multiple choices.

8. **✅Mark the Correct Choice**:
   For each choice, check the **Correct** box for the correct answer.

9. **💾Save the Question and Choices**.
