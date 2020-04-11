from haystack import indexes
from .models import Post

class LookPost(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post
    def home_look(self, using=None):
        return self.get_model().objects.all()

