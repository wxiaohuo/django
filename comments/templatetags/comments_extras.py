from django import template
from ..forms import CommentForm

register = template.Library()

@register.inclusion_tag('comments/inclusions/cf.html', takes_context=True)
def pinglun_biaodan(context, blog, biaodan=None):
    if biaodan is None:
        biaodan = CommentForm()
    return {
        'biaodan': biaodan,
        'blog': blog,
    }

@register.inclusion_tag('comments/inclusions/cl.html', takes_context=True)
def pinglun_(context, post):
    liebiao = post.comment_set.all().order_by('-created')
    total = liebiao.count()
    return {
        'total': total,
        'liebiao': liebiao,
    }