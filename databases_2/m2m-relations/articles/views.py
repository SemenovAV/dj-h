from articles.models import Article
from django.shortcuts import render


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {
        'object_list': Article.objects.all().prefetch_related('relationship_set').order_by(ordering)
    }
    return render(request, template, context)
