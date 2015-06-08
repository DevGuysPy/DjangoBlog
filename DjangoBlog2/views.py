from django.shortcuts import render, redirect, render_to_response
from .models import Article
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User

def index(request):
    if request.method == "POST":
        new_article_title = request.POST['title']
        new_article_text = request.POST['text']
        Article.objects.create(title=new_article_title, text=new_article_text, author=request.user)

    ctx = {
        'articles' : reversed(Article.objects.all()),
    }

    return render(request, 'index.html', ctx)


def add_like(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404()
    return JsonResponse({
        'status': 'OK',
        'count': article.likes
    })
    # return redirect('articles/addlike/')


def article_detail(request, article_id=1):
    return render_to_response ('article.html', {'article': Article.objects.get(id = article_id)})

def registration(request):
    user_name = request.POST.get['username']
    email_adress = request.POST.get['email']
    password = request.POST.get['password']
    User.objects.user(username=user_name, email=email_adress, password=password)
    return render(request, 'registration/registration.html')