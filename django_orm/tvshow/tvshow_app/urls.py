from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show', views.add_new),
    path('shows/<int:id>', views.create),
]