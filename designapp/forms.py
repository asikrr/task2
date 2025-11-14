from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    user_agreement = forms.BooleanField(label='Согласие на обработку персональных данных')

    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'password1', 'password2']
        labels = {'full_name': 'ФИО', 'username': 'Логин'}
        help_texts = {'full_name': 'Только кириллические буквы, дефис и пробелы', 'username': 'Только латиница и дефис',}