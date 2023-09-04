from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "anons", "full_text", "date"]

        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Названия статьи"}),
            "anons": TextInput(attrs={"class": "form-control", "placeholder": "Анонс"}),
            "full_text": Textarea(attrs={"class": "form-control", "placeholder": "Текст статьи"}),
            "date": DateTimeInput(attrs={"class": "form-control", "placeholder": "Дата публикаци"}),
        }
