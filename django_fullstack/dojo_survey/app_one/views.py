from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def submit_form(request):

    context = {
        "fname": request.POST['fname'],
        "lname": request.POST['lname'],
        "location": request.POST['location'],
        "language": request.POST['language'],
        "inlineRadioOptions": request.POST['inlineRadioOptions'],
        "text": request.POST['text'],
        "checkbox": request.POST['checkbox'],
    }
    
    return render(request, "show.html", context)
