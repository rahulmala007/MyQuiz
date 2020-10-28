from django.db import models
from django.forms import ModelForm
# from .models import QuizUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=False,label="Email Address")

    class Meta:
        model=User
        fields=("username", "first_name","last_name","email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email','password1', 'password2']:
            self.fields[fieldname].help_text = None

   

# class UserForm(ModelForm):
#     class Meta:
#         model=QuizUser
#         fields=['user','contact_no','dob']
#         widgets = {
#             'dob': DateInput(),
#         }


         