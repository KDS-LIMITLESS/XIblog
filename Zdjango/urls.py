"""Zdjango URL Configuration

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
from django.contrib.auth import views as authV
from django.urls import include, path
from Zblog import views

urlpatterns = [
    path('register/', include('Zblog.urls')),
    path('login/', authV.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', authV.LogoutView.as_view(template_name="logout.html"), name='logout'),

    path('password-reset/', authV.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset-done/', authV.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', authV.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', authV.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('', views.index, name="index"),
    path('comment_sent/', views.comment_sent, name="comment_sent"),
    path('admin/', admin.site.urls),
]
