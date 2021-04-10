from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.new),
    path('new', views.add_show),
    path('shows/<int:id>', views.view_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('update/<int:id>', views.update),
    path('shows/<int:id>/delete', views.delete),
]