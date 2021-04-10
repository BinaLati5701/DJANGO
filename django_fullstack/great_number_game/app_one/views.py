from django.shortcuts import render, redirect
from random import randint

def index(request):

    if 'count' not in request.session:
        request.session['count'] = 0
    if 'results' not in request.session:
        request.session['results'] = ''
    if 'rand' not in request.session:
        request.session['rand'] = randint(1, 100)
    print(request.session['rand'])

    context = {
        'results': request.session['results'],
        'count': request.session['count'],
    }
    return render(request, "index.html", context)

def guess(request):
    print(request.POST)
    request.session['count'] +=1
    
    if int(request.POST['number']) < request.session['rand']:
        request.session['results'] = "Too low!"
    elif int(request.POST['number']) > request.session['rand']:
        request.session['results'] = "Too high!" 
    else:
        request.session['results'] = "Correct!" 
    return redirect('/')

def redo(request):
    request.session.clear()
    return redirect('/')
