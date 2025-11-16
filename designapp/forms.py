import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUser, DesignRequest


class SignupForm(UserCreationForm):
    user_agreement = forms.BooleanField(label='Согласие на обработку персональных данных')

    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'password1', 'password2']
        labels = {'full_name': 'ФИО', 'username': 'Логин'}
        help_texts = {'full_name': 'Только кириллические буквы, дефис и пробелы', 'username': 'Только латиница и дефис',}

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if full_name:
            if not re.match(r'^[а-яёА-ЯЁ\s-]+$', full_name.strip()):
                raise ValidationError('ФИО может содержать только кириллические буквы, пробелы и дефисы ')
        return full_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if not re.match(r'^[a-zA-Z-]+$', username):
                raise ValidationError('Логин может содержать только латинские буквы, цифры и дефис')
        return username


class DesignRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['status', 'comment', 'result_image']

    def clean(self):
        cleaned_data = super().clean()
        new_status = cleaned_data.get('status')
        old_status = self.instance.status
        comment = cleaned_data.get('comment')
        result_image = cleaned_data.get('result_image')

        if old_status in ['w', 'd']:
            raise ValidationError('Нельзя изменить статус у заявки со статусом "Принято в работу" или "Выполнено"')

        if old_status == 'n':
            if new_status == 'd':
                if not result_image:
                    raise ValidationError('Для смены статуса на "Выполнено" нужно прикрепить изображение результата')
            elif new_status == 'w':
                if not comment:
                    raise ValidationError(
                        'Для смены статуса на "Принято в работу" нужно указать комментарий')

        return cleaned_data