from django.db import models
from login.models import User
from django.urls import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify

# Create your models here.

#栏目
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=128)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('column',args=(self.slug,))

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']



#文章
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=256)
    slug = models.SlugField('slug', max_length=60, blank=True)
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='作者', on_delete=models.CASCADE)
    photo = models.URLField(blank=True)
    content = models.TextField('内容', default='', blank=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    #当id或slug为空时，利用unidecode对中文解码，利用slugify方法根据标题手动生成slug
    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(unidecode(self.title))

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug))

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
