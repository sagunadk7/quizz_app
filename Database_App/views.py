import random
from .models import Question, UserPerformance
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid Username.')
            return redirect('login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login') 
        else:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already registered.')
            return redirect('signup')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Account created successfully.')
        return redirect('signup')
    return render(request, 'signup.html')

@login_required(login_url='/login/')
def dashboard(request):
    try:
        user_performance = UserPerformance.objects.get(user=request.user)
    except UserPerformance.DoesNotExist:
        user_performance = None
    return render(request, 'dashboard.html', {
        'user_performance': user_performance
    })

@login_required(login_url='/login/')
def take_quiz(request):
    if request.method == "POST":
        question_id = request.session.get('current_question_id')
        question = get_object_or_404(Question, id=question_id)
        selected_answer = request.POST.get('answer')
        user_performance, created = UserPerformance.objects.get_or_create(user=request.user)
        user_performance.total_attempted += 1
        if selected_answer == question.correct_answer:
            user_performance.correct_answers += 1
        user_performance.update_score()
        request.session['result'] = {
            'question_text': question.question_text,
            'selected_answer': selected_answer,
            'correct_answer': question.correct_answer,
            'is_correct': selected_answer == question.correct_answer,
        }
        question = random.choice(Question.objects.all())
        request.session['current_question_id'] = question.id
        return redirect('quiz_result')
    question = random.choice(Question.objects.all())
    request.session['current_question_id'] = question.id
    return render(request, 'quiz.html', {'question': question})

@login_required(login_url='/login/')
def quiz_result(request):
    result = request.session.get('result')
    if not result:
        return redirect('take_quiz')
    return render(request, 'quiz_result.html', {'result': result})
