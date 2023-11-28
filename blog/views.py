from django.shortcuts import render


# Create your views here.
from django.utils import timezone

from blog.models import Article


def post_list(request):
    article = Article.objects.filter(updated_date__lte=timezone.now()).order_by('updated_date').first()
    return render(request, 'blog/Article_base.html', {'article': article})
