from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model= Author
#         fields = '__all__'

class RegistrationForm(UserCreationForm):
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']


class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email']