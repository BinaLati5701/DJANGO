from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        "dojos": Dojo.objects.all(),
    }
    return render(request, "index.html", context)

def new_dojo(request):
    print(request.POST)
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        

    )
    return redirect('/')

def new_ninja(request):
    print(request.POST)

    dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = dojo
        

    )
    return redirect('/')
