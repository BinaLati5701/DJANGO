from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('books', views.books),
    path('login', views.login),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>', views.view_book),
    path('unlike/<int:id>', views.unlike_book),
    path('like/<int:id>', views.like_book),
    path('delete/<int:id>', views.delete_book),
    path('editbook/<int:id>', views.edit_book),

    

    
    
]