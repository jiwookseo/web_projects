from django import forms
from .models import Movie, Score


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'audience', 'poster_url', 'description', 'genre']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Title'
                }
            ),
            'audience': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Audience'
                }
            ),
            'poster_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Poster URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 7,
                    'placeholder': 'Enter Description'
                }
            ),
            'genre': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select Genre'
                }
            ),
        }


class ScoreModelForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['score', 'content', 'movie']
        widgets = {
            'score': forms.NumberInput(
                attrs={
                    'class': 'form-control my-1',
                    'placeholder': 'Score',
                    'min': 0,
                    'max': 10,
                    'step': 1
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control my-1',
                    'placeholder': 'Content',
                    'style': 'width: 280px'
                }
            ),
            'movie': forms.HiddenInput()
        }
