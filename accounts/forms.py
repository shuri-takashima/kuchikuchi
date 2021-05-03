from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # customuserでusernameの欄をemailにしているため。
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'メールアドレス'
            self.fields['username'].label = ''
            self.fields['password'].widget.attrs['class'] = 'form-control'
            self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
            self.fields['password'].label = ''


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ユーザー名'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'メールアドレス'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file img_preview_form',
                'placeholder': 'プロフィール画像'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'パスワード'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '確認用パスワード'
            }),
        }
        labels = {
            'username': '',
            'email': '',
            'avatar': 'プロフィール画像',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = '確認用パスワード'
        self.fields['password2'].help_text = ''

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        IMG_WIDTH = 200
        IMG_HEIGHT = 200
        IMG_SIZE = 2 * 1000 * 1000

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
                % (IMG_SIZE // 1000 // 1000)
            )

        return avatar


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ユーザー名',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'メールアドレス'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file img_preview_form',
                'placeholder': 'プロフィール画像'
            })
        }
        labels = {
            'username': '',
            'email': '',
            'avatar': '',
        }
