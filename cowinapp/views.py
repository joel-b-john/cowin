from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from cowinapp.models import Slot


def index(request):
    return render(request,'home.html')

def book(request):
    if request.method =='POST':
        name=request.POST['pname']
        number=request.POST['phn']
        date = request.POST['date']
        vaccine = request.POST['vaccine']
        district = request.POST['district']
        place = request.POST['place']
        token ='1'
        if User.objects.filter(name=name).exists():
            messages.info(request, "name Taken")
            return redirect('book')
        elif User.objects.filter(number=number).exists():
            messages.info(request, "number Taken")
            return redirect('book')
        else:
            add=Slot(name=name,number=number,date=date,vaccine=vaccine,district=district,place=place,token=token)
            add.save()
            return redirect('token')
    return render(request,'book.html')

def signup(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender = request.POST['gen']
        email = request.POST['email']
        username = request.POST['username']
        psw = request.POST['password']
        cpsw = request.POST['cpassword']
        if psw == cpsw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=psw)
                user.save()
                print("user created")
        else:
            print("password not match")
            messages.info(request, "password not match")
            return redirect('signup')
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('views',)
        else:
            messages.info(request,"invalid username & password")
            return redirect('login')
    return render(request,'login.html')

def views(request):

    return render(request,'views.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def token(request):
    return render(request, 'token.html')