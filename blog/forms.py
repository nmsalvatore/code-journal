from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'autocomplete': 'off',
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'What\'s on your mind?',
                'autocomplete': 'off',
                'data-lpignore': 'true'
            })
        }