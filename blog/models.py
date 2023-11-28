import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
from blog.common.constant import TXT_TYPE


class Article(models.Model):
    """
    文章
    """
    uuid = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=200)
    article_type = models.CharField(choices=TXT_TYPE, max_length=10)
    article_tag = models.CharField(max_length=200, null=True)
    article_url = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    del_flag = models.BooleanField(default=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.article_title
