import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import News


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Введите пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Введите пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Почта', 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
        

# class NewsForm(forms.Form):
    # title = forms.CharField(
    #     max_length=100, 
    #     label='Название', 
    #     widget=forms.TextInput(attrs={"class": "form-control"})
    # )
    # content = forms.CharField(
    #     label='Текст', 
    #     required=False, 
    #     widget=forms.Textarea(attrs={"class": "form-control"})
    # )
    # is_published = forms.BooleanField(
    #     label='Опубликовать сейчас?', 
    #     initial=True, 
    #     widget=forms.CheckboxInput(attrs={"class": "form-control"})
    # )
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(), 
    #     empty_label='Выберите категорию', 
    #     label='Категория', 
    #     widget=forms.Select(attrs={"class": "form-control"})
    # )

