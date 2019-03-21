from django import forms
from .models import Shout

# ShoutForm : Shout 모델에 기반하여, django가 만들어주는 form
class ShoutForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
class ShoutModelForm(forms.ModelForm):
    class Meta:
        model = Shout
        exclude = ['user']
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            'content': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'rows': 7,
                    'placeholder': 'Enter content'
                }
            ),
        }
