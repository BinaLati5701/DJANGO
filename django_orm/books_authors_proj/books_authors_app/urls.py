from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.add_book),
    path('books/<int:id>', views.view_book),
    path('books_add_author/<int:id>', views.select_author),
    path('authors', views.authors),
    path('add_author', views.add_author),    
    path('authors/<int:id>', views.view_author),
    path('authors_add_book/<int:id>', views.select_book),
    
]