from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "index.html")

# =============================================
# REGISTER
# ==============================================

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/')
    else: 
        # create User
        hash = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email=request.POST['email'],
            password = hash
        )
        request.session['userid'] = new_user.id
        return redirect('/books') 
# =============================================
# LOGIN
# ==============================================
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/')
    else: 
        user = User.objects.filter(email=request.POST['log_email'])
        request.session['userid'] = user[0].id
    return redirect('/books')
# =============================================
#LOG OUT
# ==============================================
def logout(request):
    request.session.clear()
    return redirect('/')

# =============================================
#BOOKS
# ==============================================
def books(request):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),
        "books" : Book.objects.all()

    }
    return render(request, "books.html", context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/books')
    else:
        logged_in = request.session['userid']
        uploaded_by=User.objects.get(id=logged_in)
        new_book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['desc'],
            uploaded_by = uploaded_by
            
        )
        new_book.users_who_like.add(uploaded_by)
        return redirect('/books')

    