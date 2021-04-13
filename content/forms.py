from django import forms
from .models import Content, Comment
import os.path

VALID_EXTENSIONS = ['.mp4', '.MP4']

class ContentCreate(forms.ModelForm):
    class Meta:
        model = Content
        fields =('title', 'introduction', 'upload', 'urls')
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form^control'}),
            'introduction': forms.Textarea(attrs={'class': 'form-control'}),
            'upload': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'urls': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'タイトル',
            'introduction': '説明',
            'upload': 'アップロード',
            'urls': 'URL',
        }


class ContentEdit(forms.ModelForm):
    class Meta:
        model = Content
        fields =('title', 'introduction', 'urls')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'introduction': forms.Textarea(attrs={'class': 'form^control'}),
            'urls': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'タイトル',
            'introduction': '説明',
            'upload': 'アップロード',
            'urls': 'URL',
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
                'placeholder': 'コメント',
            })
        }

class FindForm(forms.Form):
    find = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'search', 'class': 'form-control'})
    )