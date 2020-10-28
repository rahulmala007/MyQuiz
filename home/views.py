from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.context_processors import hasGroup

# Create your views here.
@login_required
def home(request):
    context={}
    context['isAdmin']=False
    context['isUser']=False
    if hasGroup(request.user, 'Admin'):
        context['isAdmin']=True
    else:
        context['isUser']=True
    context['user']=request.user
    return render(request, 'home/home.html',context)