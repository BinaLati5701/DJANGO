from django.shortcuts import render, redirect
from django.contrib import messages
import random
from time import strftime

def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, "index.html")



def process_money(request):
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            earnings = random.randint(10,20)
            time = strftime("%a, %b %d, %Y  %H:%M %p")
            request.session['gold'] += earnings
            request.session['activities'].append('Earned ' + str(earnings) + ' gold from the farm ' + time)
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')    
        elif request.POST['building'] == 'cave':
            earnings = random.randint(5,10)
            time = strftime("%a, %b %d, %Y  %H:%M %p")
            request.session['gold'] += earnings
            request.session['activities'].append('Earned ' + str(earnings) + ' gold from the cave ' + time)
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['building'] == 'house':
            earnings = random.randint(8,15)
            time = strftime("%a, %b %d, %Y  %H:%M %p")
            request.session['gold'] += earnings
            request.session['activities'].append('Earned ' + str(earnings) + ' gold from the house ' + time)
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['building'] == 'casino':
            earnings = random.randint(-50,50)
            time = strftime("%a, %b %d, %Y  %H:%M %p")
            request.session['gold'] += earnings
            if earnings > 0:
                request.session['activities'].append('Entered a casino and won  ' + str(earnings) + ' Ouch... ' + time)
                if len(request.session['activities']) >= 8:
                    request.session['activities'].pop(0)
                return redirect('/')
            else:
                request.session['activities'].append('Entered a casino and lost ' + str(earnings) + ' Ouch... ' + time)
                if len(request.session['activities']) >=8:
                    request.session['activities'].pop(0)
                return redirect('/')
    else:
        return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')
