from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'content', 'music']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3',
                }
            ),
        }
        labels = {
            'title': '',
            'content': '',
            'music': '',
        }