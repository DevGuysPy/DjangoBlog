from django.shortcuts import render, redirect
from .models import Article
from django.core.exceptions import ObjectDoesNotExist

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
	
def addlike (request, article_id):
	try:
		article = Article.objects.get(id=article_id)
		article.article_likes += 1
		article.save()	
	except ObjectDoesNotExist:
		raise Http404
	return redirect('articles/addlike/')	

