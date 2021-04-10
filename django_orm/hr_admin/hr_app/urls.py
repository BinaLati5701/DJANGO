from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('main', views.main),
    path('dashboard', views.human_resources),
    path('logout', views.logout),
    path('locations', views.location),
    path('departments', views.department),
    path('jobs', views.job),
    path('employees', views.employee),
    path('employee/<int:employee_id>', views.employee_info),
    path('employee_profile/<int:employee_id>', views.employee_profile),
    path('history', views.job_history),
    path('careers', views.career),
    path("apply_for_job", views.submit_resume),


]