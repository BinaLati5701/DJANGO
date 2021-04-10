from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "index.html", context)

# ================================================
# Click Show
# ================================================
def click_show(request, id):
    this_show = Show.objects.get(id=id)
    return redirect('/view_show/{id}')

# ===============================================
#  View Show
# ===============================================

def view_show(request, id):
    context = {
        "this_show" : Show.objects.get(id=id)     
    }
    return render(request, "show.html", context)

