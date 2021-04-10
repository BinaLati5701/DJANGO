from django.shortcuts import render, redirect
from .models import *


def index(request):
    context={
        "shows": Show.objects.all()
    }
    return render(request, "index.html")

# ===============================================
#  Add New Show
# ===============================================

def add_new(request):
    return render(request, "new.html")
    
def create(request, id):
    Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['rel_date'],
            description = new_showrequest.POST['desc'],
    )
    return redirect('/shows/{id}')


# ===================================================
# Create
# ===================================================
