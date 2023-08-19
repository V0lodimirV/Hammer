"""
URL configuration for phone_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main.views import (
    AuthorizeUserView,
    UserProfileView,
    UsersWithInviteListView,
    VerifyCodeView,
    ActivateInviteCodeView,
)
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("authorize/", AuthorizeUserView.as_view(), name="authorize_user"),
    path("verify_code/", VerifyCodeView.as_view(), name="verify_code"),
    path(
        "activate_invite_code/<str:phone_number>/",
        ActivateInviteCodeView.as_view(),
        name="activate_invite_code",
    ),
    path(
        "user_profile/<str:phone_number>/",
        UserProfileView.as_view(),
        name="user_profile",
    ),
    path(
        "users_with_invite/<str:phone_number>/",
        UsersWithInviteListView.as_view(),
        name="users_with_invite",
    ),
]

admin.site.site_header = "Hammer Systems ADMIN"
admin.site.site_title = "Hammer_systems_phone_auth"
admin.site.index_title = "Добро Пожаловать в админку Hammer Systems"

urlpatterns += doc_urls
