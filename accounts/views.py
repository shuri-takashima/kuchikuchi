from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from .forms import SignupForm, ProfileEditForm, LoginForm
from .models import CustomUser

class SignupView(generic.CreateView):
    model = CustomUser
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '新規登録できました！')
        return super().form_valid(form)

class ProfileEdit(generic.UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    success_url = reverse_lazy('content:index')
    template_name = 'registration/profile_edit.html'

    # ログインしているユーザが作ったもでなければアクセス不可
    def get_queryset(self):
        # このビューで生成されるベースとなるクエリセットを取得
        base_qs = super(ProfileEdit, self).get_queryset()
        # さらにユーザIDで絞った結果を返す。(存在しないので404が返る)
        # 条件分岐してエラーページを出しても可
        return base_qs.filter(id=self.request.user.id)

    def form_valid(self, form):
        messages.success(self.request, '投稿編集完了!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '投稿編集できませんでした。')
        return super().form_invalid(form)

class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
