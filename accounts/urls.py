from django.urls import path


from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('profile/edit/<int:pk>', views.ProfileEdit.as_view(), name='profile_edit'),
    path('login', views.Login.as_view(), name='login'),

]