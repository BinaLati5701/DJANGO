from django.shortcuts import render, redirect
from .models import *




# ====================================================
#                   All Shows
# =====================================================
def index(request):
    context = {
        "shows" : Show.objects.all()
    }
    return render(request, "index.html", context)

# =======================================================
#                   View Show  
# ========================================================

def show(request, id):
    context = {
        "this_show" : Show.objects.get(id=id)     
    }
    return render(request, "show.html", context)
