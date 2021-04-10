from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/')
    else: 
        # create User
        hash1 = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            password = hash1,
        
        )
        # once created, Log them in
        request.session['userid'] = new_user.id
        messages.success(request, "Successfully Registered!")
        return redirect('/success') 
        
def login(request):
    # validate that user exists
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/')
    else: 
        user = User.objects.filter(email=request.POST['log_email'])
        request.session['userid'] = user[0].id
        messages.success(request, "Successfully Logged In!")
        return redirect('/success')

def success(request): 
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    context = {
    "logged_in": User.objects.get(id=request.session['userid'])
    }

    return render(request, "success.html", context)

def logout(request):
    request.session.clear()
    messages.success(request, "Successfully logged out!")
    return redirect('/')   



    


