from django import template
from django.db.models import Count

from ..models import Post


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag(filename="blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-published_at")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    # Aggregate the total number of comments for each post
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]