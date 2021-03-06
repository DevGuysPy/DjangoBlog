"""DjangoBlog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import index, article_detail, like_article, like_comment, registration, new_article, add_comment

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="index"),
    url(r'^new/$', new_article, name='new_article'),
    url(r'^registration/$', registration, name="registration"),
    url(r'^articles/(?P<article_id>\d+)/$', article_detail, name='article_detail'),
    url(r'^articles/(?P<article_id>\d+)/addlike/$', like_article, name='like_article'),
    url(r'^articles/(?P<article_id>\d+)/comments/(?P<comment_id>\d+)/addlike/$', like_comment, name="like_comment"),
    url(r'^articles/(?P<article_id>\d+)/addcomment/$', add_comment, name='add_comment'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),

]
