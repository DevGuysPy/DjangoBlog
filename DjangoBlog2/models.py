from django.db import models

class Message(models.Model):
	article_title = models.CharField(max_length= 100)
	article_text = modles.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField()

	class Meta():
		db_table = 'articles'