from django import forms
from .models import News
# from .models import Category
import re
from django.core.exceptions import ValidationError


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

