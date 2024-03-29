from django.shortcuts import render

from .models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article = Article.objects.all()
    context = {'articles': article}
    print(article)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)