from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=25)
    release_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
