from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('books', views.books),
    path('login', views.login),
    path('logout', views.logout),
    path('add_book', views.add_book),
    # path('view_book/<int:id>', views.view_book),
    
    
]