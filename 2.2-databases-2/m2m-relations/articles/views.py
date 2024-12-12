from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering)
    for article in articles:
        article.scopes_sorted = sorted(
            article.scopes.all().select_related('tag'),
            key=lambda scope: (not scope.is_main, scope.tag.name)
        )
    context = {'object_list': articles}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
