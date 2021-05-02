from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q

from accounts.models import CustomUser, Connection
from .models import Content, Comment, Good
from .forms import ContentCreate, ContentEdit, CommentForm, FindForm

def index(request):
    if request.user.is_authenticated:
        connection = Connection.objects.filter(following=request.user)
        followers = [c.follower for c in connection]
        contents = Content.objects.filter(owner__in=followers).order_by('created_at').reverse()
        items = Content.objects.exclude(owner__in=followers).order_by('views_count').reverse()
    else:
        contents = Content.objects.all().order_by('views_count').reverse()
        items = None
    params ={
        'contents': contents,
        'items': items,
    }
    return render(request, 'content/index.html', params)

def show(request, pk):
    content = get_object_or_404(Content, id=pk)
    comments = Comment.objects.filter(content=content).order_by('created_at').reverse()
    is_good = Good.objects.filter(owner=request.user).filter(content=content)
    #SHOWを訪れた時の視聴回数
    content.views_count +=1
    content.save()
    good_count = Good.objects.filter(content=content).count()
    params ={
        'content': content,
        'form': CommentForm,
        'comments': comments,
        'good_count': good_count,
        'is_good': is_good,
    }
    return render(request, 'content/show.html', params)

def comment_btn(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = get_object_or_404(Content, pk=request.POST.get('content_id'))
            owner = request.user
            comment = request.POST.get('comment')
            new = Comment(
                content=content,
                owner=owner,
                comment=comment,
            )
            new.save()
            params = {
                'content_id': content.id,
                'comment': new.comment,
                'username': new.owner.username,
                'avatar_url': new.owner.avatar.url,
            }

        if request.is_ajax():
            return JsonResponse(params)

def good_btn(request):
    if request.method == 'POST':
        content = get_object_or_404(Content, pk=request.POST.get('content_id'))
        owner = request.user
        gooded = False
        good =Good.objects.filter(
            owner=owner,
            content=content,
        )
        if good.exists():
            good.delete()
        else:
            good.create(
                owner=owner,
                content=content,
            )
            gooded = True
        params ={
            'content_id': content.id,
            'gooded': gooded,
            'count': content.good_set.count(),
        }

        if request.is_ajax():
            return JsonResponse(params)

class Create(LoginRequiredMixin, generic.CreateView):
    model = Content
    template_name ='content/create.html'
    form_class = ContentCreate
    success_url = reverse_lazy('content:index')
    def form_valid(self, form):
        content = form.save(commit=False)
        content.owner = self.request.user
        content.save()
        messages.success(self.request, '投稿完了！！')
        #このform_validがsuccess_urlのURLを指している。
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, '投稿できませんでした。')
        return super().form_invalid(form)

class Edit(LoginRequiredMixin, generic.UpdateView):
    model = Content
    template_name ='content/edit.html'
    form_class = ContentEdit

    # success_url と get_success_urlの違い
    # ↑静的なページ　　　↑動的なページ　遷移のちがいである。
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'content:show',
            kwargs={'pk' :self.kwargs['pk']}
        )

    # ログインしているユーザが作ったもでなければアクセス不可
    def get_queryset(self):
        # このビューで生成されるベースとなるクエリセットを取得
        base_qs = super(Edit, self).get_queryset()
        # さらにユーザIDで絞った結果を返す。(存在しないので404が返る)
        # 条件分岐してエラーページを出しても可
        return base_qs.filter(owner=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, '投稿編集完了!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, '投稿編集できませんでした。')
        return super().form_invalid(form)


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Content
    template_name ='content/delete.html'
    success_url = reverse_lazy('content:index')

    def get_queryset(self):
        # このビューで生成されるベースとなるクエリセットを取得
        base_qs = super(Delete, self).get_queryset()
        # さらにユーザIDで絞った結果を返す。(存在しないので404が返る)
        # 条件分岐してエラーページを出しても可
        return base_qs.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '投稿を削除しました。')
        return super().delete(request, *args, **kwargs)


@login_required(login_url='/accounts/login/')
def profile(request, pk):
    contents = Content.objects.filter(owner_id=pk)
    user = get_object_or_404(CustomUser, id=pk)
    following_count = Connection.objects.filter(following_id=pk).count()
    follower_count = Connection.objects.filter(follower_id=pk).count()

    #自分がこのユーザーをfollowしているのか否かを調べる。
    check = Connection.objects.filter(follower=user, following=request.user)
    params = {
        'contents': contents,
        'user': user,
        'following_count': following_count,
        'follower_count': follower_count,
        'check': check,
    }
    return render(request, 'content/profile.html', params)

def connection_btn(request):
    if request.method == 'POST':
        follower = get_object_or_404(CustomUser, pk=request.POST.get('user_id'))
        following = request.user
        checked = False
        connection = Connection.objects.filter(
            following=following,
            follower=follower,
        )
        if connection.exists():
            connection.delete()
        else:
            connection.create(
                following=following,
                follower=follower,
            )
            checked = True

        params = {
            'checked': checked,
            'follower_count': Connection.objects.filter(follower=follower).count(),
        }

        if request.is_ajax():
            return JsonResponse(params)


@login_required(login_url='/accounts/login/')
def good(request):
    goods = Good.objects.filter(owner=request.user)

    return render(request, 'content/good.html', {'goods': goods})

class Following(LoginRequiredMixin, generic.TemplateView):
    template_name='content/following.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['followings'] = Connection.objects.filter(following_id=self.kwargs['pk'])
        context['person'] = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        return context

class Follower(LoginRequiredMixin, generic.TemplateView):
    template_name='content/follower.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['followers'] = Connection.objects.filter(follower_id=self.kwargs['pk'])
        context['person'] = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        return context

def find(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        find = request.POST['find']
        content = Content.objects.filter(
            Q(title__contains=find)|
            Q(introduction__contains=find)|
            Q(owner__username__contains=find)
            ).order_by('views_count').reverse()
        msg = '検索結果' + str(content.count()) +'件'
    else:
        msg ='' 
        content = Content.objects.all().order_by('views_count').reverse()
        form = FindForm()
    params = {
        'msg': msg,
        'form': form,
        'contents': content,
    }
    return render(request, 'content/find.html', params)