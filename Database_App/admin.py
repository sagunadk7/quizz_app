from django.contrib import admin
from django.contrib import admin
from .models import UserPerformance, Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question_text','choices','correct_answer']
@admin.register(UserPerformance)
class UserPerformanceAdmin(admin.ModelAdmin):   
    list_display = ['id','total_attempted','correct_answers','score']

