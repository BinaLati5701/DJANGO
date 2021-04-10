from django.shortcuts import render, redirect
from .models import *

def index(request):
    context ={
        "books": Book.objects.all()   
        
    }
    return render(request, "index.html", context)

def add_book(request):
    print(request.POST)
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
    )
    return redirect('/')

def view_book(request, id):

    context = {
        "books": Book.objects.get(id=id),
        "authors": Book.objects.get(id=id).authors.all(),
        "all_authors": Author.objects.all()
    }
    
    return render(request, "books.html", context)

def select_author(request, id):
    print(request.POST)

    this_author = Author.objects.get(id=request.POST['select_author'])
    this_book = Book.objects.get(id=id).authors.add(this_author)
        
    return redirect(f'/books/{id}')

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    print(request.POST)
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect(f'/authors')

def view_author(request, id):
    context = {
        "authors": Author.objects.get(id=id),
        "books": Author.objects.get(id=id).books.all(),
        "all_books": Book.objects.all()
    }
    return render(request, "authors_info.html", context)

def select_book(request, id):
    print(request.POST)

    this_book = Book.objects.get(id=request.POST['select_book'])
    this_author = Author.objects.get(id=id).books.add(this_book)
        
    return redirect(f'/authors/{id}')








    







