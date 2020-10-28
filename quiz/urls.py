from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_quizzes/', showQuizzes,name='all_quiz'),
    path('all_quizzes/<int:id>/', show_quiz,name='show_quiz'),
    path('takeQuiz/<int:id>/',takeQuiz,name='take_quiz'),
    path('submitQuiz/',submitQuiz,name='submit_quiz'),
    path('createQuiz',createQuiz,name='create_quiz'),
    path('showQuizAdmin/<int:id>',showQuizAdmin,name='showQuizAdmin'),
]