"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_views.archive, name='archive'),
    re_path(r'^article/(?P<article_id>\d+)$', article_views.get_article, name='get_article'),
    path('article/new/', article_views.create_post, name='create_post'),
    path('auth/register/', article_views.register, name='register'),
    path('auth/login/', article_views.login_view, name='login'),
    path('auth/logout/', article_views.logout_view, name='logout'),
]
