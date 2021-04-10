from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

# ====================================================================================
# REGISTER
# ====================================================================================

def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/')
    else: 
        # create User
        hash1 = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            password = hash1,
        
        )
        # once created, Log them in
        request.session['userid'] = new_user.id
        return redirect('/dashboard') 

# ====================================================================================
# LOGIN
# ====================================================================================

def login(request):
    # validate that user exists
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)        
        return redirect('/')
    else: 
        user = User.objects.filter(email=request.POST['log_email'])
        request.session['userid'] = user[0].id
        return redirect('/dashboard')


# ====================================================================================
#LOG OUT
# ====================================================================================
def logout(request):
    request.session.clear()
    messages.success(request, "Successfully logged out!")
    return redirect('/') 

# ====================================================================================
# DASHBOARD
# ====================================================================================

def dashboard(request):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),       
        "trips": Trip.objects.all()       
    
    }

    return render(request, "dashboard.html", context)

# ====================================================================================
# ADD NEW TRIP
# ====================================================================================

def new_trip(request):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),           

    }

    return render(request, "new_trip.html", context)


def add_trip(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')   
    else:  
        logged_in = request.session['userid']
        this_user = User.objects.get(id=logged_in)      
        new_trip = Trip.objects.create(
            
            destination = request.POST['desc'],
            start_date = request.POST['s_date'],
            end_date = request.POST['e_date'],
            plan = request.POST['plan'],
            created_by=this_user                
        )
        
        return redirect('/dashboard')

# ====================================================================================
# VIEW TRIPS
# ====================================================================================
def view_trip(request, trip_id):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),
        "this_trip":  Trip.objects.get(id=trip_id),         

    }
    return render(request, "view_trip.html", context)

# ====================================================================================
# EDIT TRIPS
# ====================================================================================
def edit(request, trip_id):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),
        "this_trip":  Trip.objects.get(id=trip_id),         

    }
    return render(request, "edit_trip.html", context)


def update(request, trip_id):
    errors = Trip.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{trip_id}')   
    else: 
        t = Trip.objects.get(id=trip_id)
        t.destination = request.POST['edit_desc']
        t.start_date = request.POST['edit_sdate']
        t.end_date = request.POST['edit_edate']
        t.plan = request.POST['edit_plan']
        t.save()
        return redirect('/dashboard')

# ====================================================================================
# DELETE TRIPS
# ====================================================================================

def delete(request, trip_id):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    else:
        t = Trip.objects.get(id=trip_id)
        t.delete()    
        return redirect('/dashboard')


