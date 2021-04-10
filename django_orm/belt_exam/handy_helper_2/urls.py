from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('new_job', views.new_job),
    path('jobs/new', views.add_job),
    path('jobs/<int:job_id>', views.view_job),
    path('click_edit/<int:job_id>', views.click_edit),
    path('jobs/edit/<int:job_id>', views.edit_job),


    
]