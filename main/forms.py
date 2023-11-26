from django import forms

# форма авторизации
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль')