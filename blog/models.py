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
    uuid = models.CharField(max_length=200)  # 散列值id
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 文章作者
    article_title = models.CharField(max_length=200)  # 文章标题
    article_type = models.CharField(choices=TXT_TYPE, max_length=10)  # 文章类型
    article_tag = models.CharField(max_length=200, null=True)  # 文章标签
    article_url = models.CharField(max_length=200)  # 文章地址
    created_date = models.DateTimeField(default=timezone.now)  # 上传时间
    updated_date = models.DateTimeField(blank=True, null=True, default=timezone.now)  # 更新时间
    del_flag = models.BooleanField(default=True)  # 是否删除

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
