from django.shortcuts import render
from .models import Article

def index(request):
	
	if request.method == "POST":
		new_article_title = request.POST['title']
		new_article_text = request.POST['text']
		Article.objects.create(
			article_title=new_article_title,
			article_text=new_article_text)
	ctx = {
		'articles' : reversed(Article.objects.all()),
	}

	return render(request, 'index.html', ctx)

