"""kuchikuchi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls')),


    path('logout', views.LogoutView.as_view(), name='logout'),
    path('password_change', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uid64>/<token>', views.PasswordResetConfirmView.as_view(), name='reset'),
    path('reset/done', views.PasswordResetCompleteView.as_view(), name='reset_done'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)