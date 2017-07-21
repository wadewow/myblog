# coding:utf-8
from django.shortcuts import render
# from django.http import HttpResponse
import models
# Create your views here.


def home(request):
    '''
    下面的语句相当于 select * from article where id = 1
    '''
    articles = models.Article.objects.all()
    return render(request, 'blog/blog_home.html', {'articles': articles})


def content(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, 'blog/blog_content.html', {'article_content': article})


def edit(request,article_id):
    print 'id等于：', article_id
    if str(article_id) == '0':
        return render(request,'blog/blog_edit.html')
    article = models.Article.objects.get(pk = article_id)
    return render(request,'blog/blog_edit.html',{'article':article})


def form_action(request):
    title = request.POST.get('title')       # 这里get('title')的title是根据input的name属性值title
    content = request.POST.get('content')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title = title, content = content)
        articles = models.Article.objects.all()
        return render(request,'blog/blog_home.html',{'articles':articles})
    article = models.Article.objects.get(pk = article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/blog_content.html', {'article_content': article})
