from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('login', views.login),
    path('logout', views.logout),
    path('new', views.new_trip),
    path('add_trip', views.add_trip),
    path('view/<int:trip_id>', views.view_trip),
    path('edit/<int:trip_id>',views.edit),
    path('update/<int:trip_id>', views.update),  
    path('delete/<int:trip_id>', views.delete),
    
]