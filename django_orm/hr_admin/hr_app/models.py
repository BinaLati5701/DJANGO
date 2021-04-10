from django.core.exceptions import ValidationError
from django.db import models
import re
import bcrypt


def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError('{} must be longer than: 2'.format(value))

def validateEmailFormat(value):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(value):
        raise ValidationError('{} email must be a valid format'.format(value))
        
def validateLengthGreaterThanEight(value):
    if len(value) < 9:
        raise ValidationError('{} must be at least: 8'.format(value))
    



class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    email = models.CharField(max_length=100, validators = [validateEmailFormat])
    password = models.CharField(max_length=100, validators=[validateLengthGreaterThanEight])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class Location(models.Model):
    street_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Department(models.Model):
    department_name =models.CharField(max_length=25)
    location = models.ForeignKey(Location, related_name="departments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Job(models.Model):
    job_title = models.CharField(max_length=25)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    phone = models.IntegerField()
    hire_date = models.DateField()
    salary = models.FloatField()
    bonus = models.FloatField()
    dept_work = models.ForeignKey(Department, related_name="employees", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="employees", on_delete=models.CASCADE)
    users = models.ForeignKey(User, related_name="employees", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class JobHistory(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    employee = models.ForeignKey(Employee, related_name="job_histories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





