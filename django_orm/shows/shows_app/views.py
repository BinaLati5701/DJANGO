from django.shortcuts import render, redirect
from .models import *



def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "index.html", context)

# ======================================================
#               ADD A NEW SHOW
# =======================================================

def new(request):
    return render(request, "add_show.html")

def add_show(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['mm/dd/YYYY'],
        description = request.POST['desc']

    )
    return redirect('/')

# ===========================================================
#                   VIEW SHOW
# ============================================================

def view_show(request, id):
    context = {
        "this_show": Show.objects.get(id=id)
    }
    return render(request, "view_show.html", context)

# ==============================================================
#                   EDIT SHOW
# ===============================================================

def edit_show(request, id):
    context = {
        "this_show": Show.objects.get(id=id)
        
    }
    return render(request, "edit_show.html", context)


def update(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title'],
    show.network = request.POST['network'],
    show.release_date = request.POST['mm/dd/YYYY'],
    show.description = request.POST['desc']
    show.save()
    return redirect('/shows/{id}')

# =================================================================
#                      DELETE SHOW
# ==================================================================

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()

    return redirect('/')
