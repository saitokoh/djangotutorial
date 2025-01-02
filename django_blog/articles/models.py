from django.db import models


class Articles(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=50)
    article_body = models.TextField(verbose_name='本文', max_length=10000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)