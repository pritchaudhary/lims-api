
from django.contrib import admin
from django.urls import path, include

from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from accounts import views as accounts_views
from accounts import views


urlpatterns = [
    # path('ping/', accounts_views.PingView.as_view()),
    # path("", views.UserView.as_view(), name="users")
    path("login/", accounts_views.LoginView.as_view(),
         name="login"),


]
