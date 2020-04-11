from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):  # 继承models.Model
    tname = models.CharField(max_length=30)

    def __str__(self):
        return self.tname

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    def __str__(self):
        return self.title

    def look_up(self):
        return reverse('boke:pages', kwargs={'pk': self.pk})

    title = models.CharField('标题', max_length=30)
    content = models.TextField('正文')
    excerpt = models.CharField('摘要', max_length=100, blank=True)
    created = models.DateTimeField('创建时间')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    # 统计文章阅读量
    views = models.PositiveIntegerField(default=0)

    def statistics(self):  # 统计文章阅读量
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        # 根据时间对文章进行排序
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created']
