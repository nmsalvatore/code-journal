from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'tags',
            'body'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'autocomplete': 'off',
            }),
            'tags': forms.TextInput(attrs={
                'placeholder': 'Tags (maximum length is 10 characters, separate tags with a comma)',
                'autocomplete': 'off',
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'What\'s on your mind?',
                'autocomplete': 'off',
                'data-lpignore': 'true'
            })
        }