from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt



def index(request):
    return render(request, "homepage.html")

def register(request):
    errors = User.objects.validator(request.POST)
    
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect ('/')

    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password= pw_hash
    )
    messages.info(request, 'User Created')
    return redirect ('/')

def login (request):
    try:
        user= User.objects.get(email= request.POST['email'])
        
    except:
        print ("password or email is incorrect")
        messages.error (request, 'E-mail or Password is incorrect')    
        return redirect ('/')

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        print("password match")
    
    else:
        messages.error (request, 'E-mail or Password is incorrect')    
        return redirect ('/')

    request.session ['user_id']= user.id
    request.session ['first_name']= user.first_name
    request.session ['last_name']= user.last_name
    
    messages.info (request, "You are logged in")
    return redirect('/intel')


def logout(request):
    del request.session ['user_id']
    del request.session ['first_name']
    del request.session ['last_name']
    messages.info (request, 'You are logged out')
    return redirect('/')
