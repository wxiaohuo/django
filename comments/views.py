from boke.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.contrib import messages


@require_POST  # 装饰器
def comment(request, post_pk):
    blog = get_object_or_404(Post, pk=post_pk)
    biaodan = CommentForm(request.POST)
    if biaodan.is_valid():
        pl = biaodan.save(commit=False)
        pl.post = blog
        pl.save()
        messages.add_message(request, messages.SUCCESS,
                             '发表成功！', extra_tags='success')
        return redirect(blog)
    context = {
        'blog': blog,
        'biaodan': biaodan,
    }
    messages.add_message(request, messages.ERROR,
                         '发表失败，请重新填写！！！', extra_tags='danger')
    return render(request, 'comments/display.html', context=context)
