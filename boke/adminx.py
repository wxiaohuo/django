import xadmin
from .models import Post, Category, Tag


class BokeAdmin(object):
    list_display = ['title', 'created', 'tags', 'category', 'author']
    search_fields = ['title']


xadmin.site.register(Post, BokeAdmin)
xadmin.site.register(Category)
xadmin.site.register(Tag)
