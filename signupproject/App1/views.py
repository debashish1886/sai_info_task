from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method=="POST":
        uname=request.POST.get("n1")
        email=request.POST.get("n2")
        pswd=request.POST.get("n3")
        cpswd=request.POST.get("n4")
        if pswd!=cpswd:
            return HttpResponse("Your pswd and confirm pswd are not same!!")
        else:
            my_user=User.objects.create_user(uname,email,pswd)
            my_user.save()
            return redirect('login')


    return render(request,"signup.html")

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        paswd1=request.POST.get("password")
        user=authenticate(request,username=username,password=paswd1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username & Password is incorrect!!")

    return render(request,"login.html")


def homepage(request):
    return render(request,"homepage.html")


def logoutpage(request):
    logout(request)
    return redirect('login')