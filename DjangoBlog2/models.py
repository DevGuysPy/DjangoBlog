from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="article_likes")

    class Meta():
        db_table = 'articles'


class Comments(models.Model):
    comment_text = models.TextField()
    comment_article = models.ForeignKey(Article)
    date = models.DateTimeField(auto_now_add=True) 

    class Meta():
        db_table = 'comments'
