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
        hash = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            password = hash
        
        )
        request.session['userid'] = new_user.id      
        return redirect('/books')

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

def books(request): 
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),
        "books": Book.objects.all()
    }

    return render(request, "books.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')


def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/books')
    else:
        uploaded_by_id = request.session['userid'] 
        uploaded_by= User.objects.get(id=uploaded_by_id) 
        new_book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['desc'],
            uploaded_by = uploaded_by                 
        )
        new_book.users_who_like.add(uploaded_by)
        return redirect('/books')

def view_book(request, book_id):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "this_book": Book.objects.get(id=book_id),
        "logged_in": request.session['userid'],
        # "book_uploader_id": request.session['this_book.uploaded_by_id'],
        # "book" : this_book,
        # "users": this_book.users_who_like.all()
    }
    return render(request, "view_book.html", context)

def unlike_book(request, id):
    this_book = Book.objects.get(id=id)
    this_user = User.objects.get(id=request.session['userid'])
    this_book.users_who_like.remove(this_user)
    return redirect('/books/{id}')

def like_book(request, id):
    this_book = Book.objects.get(id=id)
    this_user = User.objects.get(id=request.session['userid'])
    this_book.users_who_like.add(this_user)
    return redirect('/books/{id}')

def edit_book(request, id):
    errors = Book.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/books/{id}')
    else:
        this_book = Book.objects.get(id=id)
        new_title = request.POST['edit_title']
        new_desc = request.POST['edit_desc']
        this_book.title = new_title
        this_book.description = new_desc
        this_book.save()
        return redirect('/books/{id}')


def delete_book(request, id):
    this_book = Book.objects.get(id=id)
    book_uploader_id = this_book.uploaded_by_id
    if(request.session['userid'] ==book_uploader_id):
        this_book.delete()
        return redirect('/books')
    else:
        return redirect('/')









