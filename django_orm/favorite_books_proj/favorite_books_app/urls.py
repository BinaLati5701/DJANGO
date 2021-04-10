from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('add_book', views.add_book),
    path('books/<int:book_id>',views.view),


    path('logout', views.logout),
]