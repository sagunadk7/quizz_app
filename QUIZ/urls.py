from django.contrib import admin
from django.urls import path
from Database_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name='dashboard'),
    path('take_quiz/',views.take_quiz, name = 'take_quiz'),
    path('quiz_result/',views.quiz_result, name = 'quiz_result'),    
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]