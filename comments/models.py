from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField('用户名', max_length=50)
    email = models.EmailField('邮箱')
    body = models.TextField('内容')
    created = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('boke.Post', verbose_name='文章', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{}: {}'.format(self.name, self.body[:20])
