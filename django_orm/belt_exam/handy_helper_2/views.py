from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "index.html")

# ==================Register New User=====================


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


# =====================Login Existing User=========================
        
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


# =====================Log Out User=====================================
def logout(request):
    request.session.clear()
    messages.success(request, "Successfully logged out!")
    return redirect('/') 

# ==================Dashboard Main Page==================================

def dashboard(request):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),       
        "jobs": Job.objects.all()       
    
    }

    return render(request, "dashboard.html", context)


# ======================New Job==========================================

def new_job(request):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')
    
    context = {
        "logged_in": User.objects.get(id=request.session['userid']),           

    }

    return render(request, "add_job.html", context)

# ================Add Job=================================================

def add_job(request):
    errors = Job.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new_job')   
    else:        
        new_job = Job.objects.create(
            user = User.objects.get(id=request.session['userid']),
            title = request.POST['title'],
            desc = request.POST['desc'],
            location = request.POST['loc']                
        )
        
        return redirect('/dashboard')

# ===================View Job ===================================================

def view_job(request, job_id):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')

    context = {
        "this_job" : Job.objects.get(id=job_id),
        "logged_in" : request.session['userid'],
    }


    return render(request, "view_job.html", context)

# ========================Edit Job ===============================================

def click_edit(request, job_id):
    if "userid" not in request.session:        
        messages.error(request, "Please log in before continuing!")
        return redirect('/')

    context = {
        "this_job" : Job.objects.get(id=job_id),
        "logged_in" : request.session['userid'],       
    }
    return render(request, "edit_job.html", context)




def edit_job(request, job_id):
    errors = Job.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/click_edit/{job_id}')   
    else:        
        j = Job.objects.get(id=job_id)
        j.title = request.POST['title']
        j.desc = request.POST['desc']
        j.location = request.POST['loc']
        j.save()                
        
        
        return redirect('/dashboard')





