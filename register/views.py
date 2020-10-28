from django.shortcuts import render
from . forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.
def start_view(request):
    return render(request,'register/start.html')

def register_view(request):
    context={};
    form=RegisterForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            user=form.save()
            groupname ,created=Group.objects.get_or_create(name='User')
            if user is not None:
                groupname.user_set.add(user)
            return redirect('/login')
    context['form']=form
    return render(request,'register/create_user.html',context)
