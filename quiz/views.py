from django.shortcuts import render
from .models import *
from question.models import *
from datetime import datetime,time,date
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home.context_processors import hasGroup
from django.contrib.auth.decorators import login_required
# Create your views here.
score=0
GLOBAL_Entry = None
@login_required
def showQuizzes(request):

    past_quizzes=quiz.objects.filter(end_time__lt=datetime.now().strftime('%H:%M:%S'),end_date__lte=date.today())
    remaining_past=quiz.objects.filter(end_date__lt=date.today())
    past_quizzes|=remaining_past
    live_quizzes=quiz.objects.filter(start_time__lte=datetime.now().strftime('%H:%M:%S'),start_date=date.today(),end_time__gte=datetime.now().strftime('%H:%M:%S'))
    upcoming_quizzes=quiz.objects.filter(start_date__gt=date.today())
    remaining=quiz.objects.filter(start_date=date.today(),start_time__gte=datetime.now().strftime('%H:%M:%S'))
    upcoming_quizzes|=remaining
    context={ 
        'past_quizzes':past_quizzes,
        'live_quizzes':live_quizzes,
        'upcoming_quizzes':upcoming_quizzes,
    }
    context['isUser']=False
    context['isAdmin']=False
    if hasGroup(request.user,'Admin'):
        context['isAdmin']=True
    else:
        context['isUser']=True
    return render(request,'quiz/show_Quizzes.html',context)

@login_required
def show_quiz(request,id):
    this_quiz=quiz.objects.get(id=id);
    open_text_questions=OpenText.objects.filter(quiz__id=id)
    mcq_questions=OpenText.objects.filter(quiz__id=id)
    context={
        'this_quiz':this_quiz,
        'open_text_questions':open_text_questions,
        'mcq_questions':mcq_questions,
        'quiz_id':id
    }
    return render(request,'quiz/quiz_detail.html',context)

@login_required
def takeQuiz(request,id):
    mcq_questions=MCQ.objects.filter(quiz__id=id)
    open_text_questions=OpenText.objects.filter(quiz__id=id)
    # all_questions=chain(mcq_questions, open_text_questions)
    context={
        'questions':mcq_questions,
        'open_questions':open_text_questions
        
    }
    return render(request,'quiz/take_quiz.html',context)

@login_required
@csrf_exempt
def submitQuiz(request):
    if request.method=='POST':
        global score
        score=0
        dict=request.POST 
        for key in dict:
            val=int(key[1:])
            if key[0]=='+':
                actual_answer=MCQ.objects.get(id=int(val)).answer_value
                my_answer=int(dict[key])
                if actual_answer== my_answer:
                    score+=1
            else:
                actual_answer=OpenText.objects.get(id=int(val)).answer_content
                my_answer=dict[key]
                if actual_answer== my_answer:
                    score+=1

    context={
        'score':score
    }
    return render(request,'quiz/score.html',context)

@login_required
def createQuiz(request):
    form=QuizForm(request.POST or None)
    if request.method=='POST':
        form=QuizForm(request.POST)
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
            quiz.objects.create(**form.cleaned_data)
            return redirect('quiz:all_quiz')
    context={
        'form':form
    }
    return render(request,'quiz/show_form.html',context);


@login_required
@csrf_exempt
def showQuizAdmin(request,id):
    all_obj=quiz.objects.filter(id=id)
    obj=all_obj[0]
    if request.method=='POST':
        
        obj.number_of_questions+=1
        dict=request.POST
        # print("hi-----")
        # print(dict)
        if dict['ismcq'] =="1":
            new_mcq=MCQ()
            new_mcq.description=dict['description1']
            new_mcq.option1=dict['option1']
            new_mcq.option2=dict['option2']
            new_mcq.option3=dict['option3']
            new_mcq.option4=dict['option4']
            new_mcq.answer_value=dict['answer_value']
            obj.save()
            new_mcq.quiz=obj
            new_mcq.save()
        else:
            new_text=OpenText()
            new_text.description=dict['description2']
            new_text.answer_content=dict['answer_content']
            obj.save()
            new_text.quiz=obj
            new_text.save() 
        return HttpResponse("OK")
    else:

        all_mcq = MCQ.objects.filter(quiz__id=id)
        all_text=OpenText.objects.filter(quiz__id=id)
        context={
            'this_quiz':obj,
            'obj_id':id,
            'all_mcq':all_mcq,
            'all_text':all_text
        }
        context['isPast']=False
        context['isLive']=False
        context['isUpcoming']=False

        past_quizzes=quiz.objects.filter(end_time__lt=datetime.now().strftime('%H:%M:%S'),end_date__lte=date.today())
        live_quizzes=quiz.objects.filter(start_time__lte=datetime.now().strftime('%H:%M:%S'),start_date__lte=date.today(),end_time__gte=datetime.now().strftime('%H:%M:%S'))
        

        if obj in past_quizzes:
            context['isPast']=True
        elif obj in live_quizzes:
            context['isLive']=True
        else:
            context['isUpcoming']=True


        return render(request,'quiz/showQuizAdmin.html',context)


    













