from django.contrib import admin
from django.urls import path, include
from content.views import  Create, Edit, Delete, Follower, Following
from . import views

app_name='content'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:pk>', views.show, name='show'),
    path('comment', views.comment_btn, name='comment_btn'),
    path('good', views.good_btn, name='good_btn'),
    path('create/', Create.as_view(), name='create'),
    path('edit/<int:pk>', Edit.as_view(), name='edit'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('good/', views.good, name='good'),
    path('following/<int:pk>', Following.as_view(), name='following'),
    path('follower/<int:pk>', Follower.as_view(), name='follower'),
    path('find', views.find, name='find'),
]
