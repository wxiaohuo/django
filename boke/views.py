from markdown.extensions.toc import TocExtension, slugify
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
import markdown
import re

# 首页 index
from django.core.paginator import Paginator  # 分页


def home(request, i=1):  # 获取全部文章
    num = int(i)
    # 获取所有文章信息（时间）
    lists = Post.objects.all().order_by('-created')
    # 创建分页器
    pj = Paginator(lists, 5)
    # 获取当前页数据
    Pa = pj.page(num)
    return render(request, 'boke/home.html', context={'article_list': Pa})


# 文章详情功能 detail
def pages(request, pk):
    i = get_object_or_404(Post, pk=pk)
    # 文章阅读量
    i.statistics()
    # 自动生成目录
    my = markdown.Markdown(extensions=['markdown.extensions.toc', TocExtension(slugify=slugify)])
    i.content = my.convert(i.content)
    wang = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', my.toc, re.S)
    i.toc = wang.group(1) if wang is not None else ''

    return render(request, 'boke/pages.html', context={'post': i})


# 归档功能 archives
def files(request, year, month):
    # 使用模型管理器filter函数来过滤文章，依据年，月
    lists = Post.objects.filter(created__year=year, created__month=month).order_by('-created')
    return render(request, 'boke/home.html', context={'article_list': lists})


# 分类功能 category
def classification(request, pk):
    dates = get_object_or_404(Category, pk=pk)
    lists = Post.objects.filter(category=dates).order_by('-created')
    return render(request, 'boke/home.html', context={'article_list': lists})
