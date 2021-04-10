from django.urls import path
from . import views

urlpatterns = [
    path('show', views.index),
    path('click_show/<int:id>', views.click_show),
    path('view_show/<int:id>', views.view_show),
]