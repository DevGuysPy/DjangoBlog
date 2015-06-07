from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)

	class Meta():
		db_table = 'articles'