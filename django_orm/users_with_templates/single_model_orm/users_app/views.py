from django.shortcuts import render, redirect
from .models import Users

def index(request):
    context = {
        "users": Users.objects.all()
    }
    return render(request, "index.html", context)

def new_user(request):
    print(request.POST)

    Users.objects.create(
        first_name = request.POST['firstName'],
        last_name = request.POST['lastName'],
        email = request.POST['email'],
        age = request.POST['age']
    )


    return redirect('/')
