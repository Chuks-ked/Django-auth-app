from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html',{

    })

def Register(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST['sname']
        user_name = request.POST['uname']
        email = request.POST.get('email')
        password = request.POST['password']

        new_user = User.objects.create_user(user_name, email, password)

        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'auth_system/register.html')

def Login(request):

    if request.method=="POST":
        user_name = request.POST.get('uname')
        password = request.POST['password']

        user = authenticate(request, username=user_name, password=password)
        if user is not  None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, User doesnt exist')


    return render(request, 'auth_system/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'auth_system/test.html')
    