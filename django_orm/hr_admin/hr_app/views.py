from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
import bcrypt
import django_google_maps

API_KEY = 'AIzaSyCKfHGyq4RlnYUPNSLDyHmTZ3DrBTH5ClE'

# =======================================================
# REGISTRATION AND LOGIN FORMS
# =======================================================
def index(request):
    form = RegistrationForm()
    signin = LoginForm()
    context = {
        "myregistrationform": form,
        "myloginform" : signin,
    }
    return render(request, "index.html", context)

# =======================================================
# REGISTRATION VALIDATION
# ========================================================
def register(request):
    
    if request.method == "POST":
        e = RegistrationForm(request.POST)       
        if e.is_valid():            
            hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash
            )
            request.session['userid'] = new_user.id
            return redirect('/main')
        else:
            e = RegistrationForm()
            e.errors
            return redirect('/')
    else:
        return render(request, "index.html", context= {'form':e})
# =======================================================
# LOGIN VALIDATION
# ========================================================            
def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)        
        if f.is_valid():            
            user = User.objects.filter(email=request.POST['email'])
            request.session['employeeid'] = user[0].id       
            return redirect('/main')
        else: 
            f = LoginForm()
            f.errors
            return redirect('/')
    else:
        return render(request, "index.html", context= {'form':f})

# =======================================================
# MAIN
# ======================================================== 
def main(request):    
    return render(request, "main.html")

def human_resources(request):
    return redirect('/main')

# =======================================================
# LOG OUT
# ======================================================== 
def logout(request):
    request.session.clear()
    return redirect('/')

# ====================================================
# LOCATIONS
# ======================================================== 
def location(request):
    context = {
        "locations": Location.objects.all()
    }
    return render(request, "location.html", context)




# =======================================================
# DEPARTMENTS
# ======================================================== 
def department(request):
    context = {
        "departments": Department.objects.all()
    }
    return render(request, "department.html", context)

# =======================================================
# JOBS
# ========================================================
def job(request):
    context = {
        "jobs": Job.objects.all()
    }
    return render(request, "job.html", context)

# =======================================================
# EMPLOYEES
# =======================================================
def employee(request):
    context = {
        "employees": Employee.objects.all()
    }
    return render(request, "employee.html", context)

def employee_info(request, employee_id):
    return redirect(f'/employee_profile/{employee_id}')

def employee_profile(request, employee_id):
    context = {
        "this_employee": Employee.objects.get(id=employee_id),
        
    }
    return render(request, "employee_info.html", context)

# =======================================================
# JOB HISTORY
# ========================================================
def job_history(request):
    context = {
        "job_histories": JobHistory.objects.all()
    }
    return render(request, "job_history.html", context)

# =======================================================
# CAREERS
# ======================================================== 
def career(request):
    context = {
        "jobs": Job.objects.all()
    }
    return render(request, "career.html", context)

def submit_resume(request):
    this_job = Job.objects.get(id=request.POST['select_job'])
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    call_time = request.POST['time_to_call']
    resume_paste = request.POST['resume']
    return redirect('/careers')









