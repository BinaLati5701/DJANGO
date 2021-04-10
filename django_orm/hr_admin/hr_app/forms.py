from django import forms
from .models import User




class RegistrationForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        
        model = User
        fields = '__all__'
        
        widgets = {
            'password': forms.PasswordInput()
            
        }

        

class LoginForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        
        model = User
        fields= ['email', 'password']

        widgets = {
            'password': forms.PasswordInput()
            

        }


        



