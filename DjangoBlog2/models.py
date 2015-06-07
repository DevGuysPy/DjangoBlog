from django.db import models

class Article(models.Model):
	article_title = models.CharField(max_length=100)
	article_text = models.TextField()
	article_date = models.DateTimeField(auto_now_add=True)
	article_likes = models.IntegerField(default=0)

	class Meta():
		db_table = 'articles'