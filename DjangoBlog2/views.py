from django.shortcuts import render, redirect, render_to_response
from .models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



def index(request):
    # Article.objects.all().delete()
    ctx = {
        'articles' : reversed(Article.objects.all()),
    }

    return render(request, 'index.html', ctx)

def new_article(request):  
    if request.method == "POST":
        new_article_title = request.POST['title']
        new_article_text = request.POST['text']
        article = Article.objects.create(title=new_article_title, text=new_article_text, author=request.user)
        return redirect('article_detail', article_id=article.id)
    return render(request, 'new_article.html')




def add_like(request, article_id):
    current_user = request.user
    try:
        article = Article.objects.get(id=article_id)
        if current_user.is_authenticated():
            user_likes = request.user.article_likes
            if article not in user_likes:
                user_likes.add(article)
            else:
                user_likes.remove(article)
            request.user.save()
    except ObjectDoesNotExist:
        raise Http404()

    return JsonResponse({
        'status': 'OK',
        'count': len(article.likes)
    })
    # return redirect('articles/addlike/')


def article_detail(request, article_id=1):
    ctx = {
        'article': Article.objects.get(id=article_id),
        'comments': Comments.objects.filter(comment_article_id=article_id),
    }
    
    return render(request, 'article.html', ctx)

def registration(request):
    if request.method == "POST":
        user_name = request.POST['username']
        email_address = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=user_name, email=email_address, password=password)
        return redirect('../login/')

    return render(request, 'registration/registration.html')

def add_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        new_comment_text = request.POST['comment_text']
        Comments.objects.create(comment_text=new_comment_text, comment_article_id=article_id)
        return redirect('article_detail', article_id=article.id) 

    return render(request, 'article.html')