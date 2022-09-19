from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars_html
from django.urls import reverse_lazy

import markdown

from .models import Post


class LatestPostsFeed(Feed):
    title = "My Blog"
    link = reverse_lazy("blog:post_list")
    description = "New posts of my blog."

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item) -> str:
        return item.title

    def item_description(self, item) -> str:
        return truncatechars_html(markdown.markdown(item.body), 30)

    def item_published_at(self, item):
        return item.published_at
