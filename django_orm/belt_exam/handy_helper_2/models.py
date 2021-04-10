from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2: 
            errors['fname'] = "First Name must be at least 2 characters"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format"
        if len(postData['pass']) < 8:
            errors['pass'] = "Password must be at least 8 characters long"
        if postData['pass'] != postData['conf_pass']:
            errors['conf_pass'] = "Password and Confirmation Password must match"     

        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['log_email'])
        if len(user) < 1: 
            errors['log_email'] = "Invalid Credentials"
        else:
            logged_user = user[0]         
            if not bcrypt.checkpw(postData['log_pass'].encode(), logged_user.password.encode()):           
                errors['log_pass'] = "Invalid Credentials"
        return errors


class JobManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3: 
            errors['title'] = "A job must consist at least 3 characters long!"
        if len(postData['desc']) < 3:
            errors['desc'] = "Description must be provided!"
            if len(postData['loc']) < 3:
                errors['loc'] = "Location must be provided!"
        return errors

        

class User(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.CharField(max_length=255)
    password =models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Job(models.Model):
    title = models.CharField(max_length=26)
    desc = models.CharField(max_length=45)
    location = models.CharField(max_length=45)

    worker = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
