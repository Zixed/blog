from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='标题')
    author = models.CharField(max_length=100, unique=True, verbose_name='作者')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='标签')
    body = models.TextField(verbose_name='内容')
    posted = models.DateField(db_index=True, auto_now_add=True, verbose_name='提交日期')

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return '/posted/{a}/{b}'.format(a=self.slug, b=self.title)
