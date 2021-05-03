from django import forms
from .models import Content, Comment
import os.path

VALID_EXTENSIONS = ['.mp4', '.MP4']

class ContentCreate(forms.ModelForm):
    class Meta:
        model = Content
        fields =('title', 'introduction', 'upload', 'urls')
        widgets ={
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'タイトル'
            }),
            'introduction': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '説明'
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': 'form-control-file file_preview_form',
                'placeholder': 'アップロードファイル',
            }),
            'urls': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL'
            }),
        }
        labels = {
            'title': '',
            'introduction': '',
            'upload': '',
            'urls': '',
        }


class ContentEdit(forms.ModelForm):
    class Meta:
        model = Content
        fields =('title', 'introduction', 'urls')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'タイトル',
            }),
            'introduction': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '説明'
            }),
            'urls': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL'
            })
        }
        labels = {
            'title': '',
            'introduction': '',
            'urls': '',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('comment',)
        labels = {
            'comment': "",
        }
        widgets = {
            'comment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'コメント',
            })
        }

class FindForm(forms.Form):
    find = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'search',
            'class': 'form-control',
        })
    )