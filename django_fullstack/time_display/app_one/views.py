from django.shortcuts import render
from time import strftime

def index(request):
    context = {
        "time":strftime("%a, %b %d, %Y  %H:%M %p")
    }
    return render(request, "index.html", context)
