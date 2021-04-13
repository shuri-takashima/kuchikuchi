from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from PIL import Image


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =('username', 'email', 'avatar')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'avatar': 'プロフィール画像',
        }

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        IMG_WIDTH = 200
        IMG_HEIGHT = 200
        IMG_SIZE = 2*1000*1000


        if not avatar:
            raise forms.ValidationError(
                'プロフィール画像を選択してください。'
            )

        if avatar.image.width < IMG_WIDTH:
            raise forms.ValidationError(
                'この画像の横幅は、%spxです。%spx以上の横幅の画像の登録をお願いします。'
                % (avatar.image.width, IMG_WIDTH)
            )

        if avatar.image.height < IMG_HEIGHT:
            raise forms.ValidationError(
                'この画像の高さは、%spxです。%spx以上の高さの画像の登録をお願いします。'
                % (avatar.image.height, IMG_HEIGHT)
            )

        if avatar.size > IMG_SIZE:
            raise forms.ValidationError(
                '画像サイズが大きすぎます。％sMBより小さいサイズの画像をお願いします。'
                % (IMG_SIZE//1000//1000)
            )

        return avatar





class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'avatar': 'プロフィール画像',
        }


