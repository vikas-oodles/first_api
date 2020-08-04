from django import forms
from .models import Profile,Address
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta():
        model = Address
        fields = '__all__'
class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)
