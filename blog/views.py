from django.shortcuts import render


# Create your views here.
from django.utils import timezone

from blog.models import Article


def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
