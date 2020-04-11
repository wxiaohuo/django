import xadmin
from .models import Comment


class CommentAdmin(object):
    list_display = ['name', 'email', 'post', 'created']
    zi_duan = ['name', 'email', 'body', 'post']


xadmin.site.register(Comment, CommentAdmin)
