from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag  # 在模板中使用语法 {% get_posts %} 调用这个函数
def get_posts(num=5):
    return Post.objects.all().order_by('-created')[:num]  # 前五篇文章


@register.simple_tag
def get_files():  # 获取每篇文章的创建时间，年和月
    return Post.objects.dates('created', 'month', order='DESC')


@register.simple_tag
def get_classification():  # 分类模板标签
    return Category.objects.all()
