from django.urls import path

from . import views
from .feeds import LatestPostsFeed


app_name = "blog"
urlpatterns = [
    path(route="", view=views.post_list_view, name="post_list"),
    # path(route="", view=views.PostListView.as_view(), name="post_list"),
    path(
        route="<int:year>/<int:month>/<int:day>/<slug:post>/",
        view=views.post_detail_view,
        name="post_detail",
    ),  # SEO-friendly URL
    path(
        route="<int:post_id>/share/",
        view=views.post_share_view,
        name="post_share",
    ),
    path(
        route="<int:post_id>/comment/",
        view=views.post_comment_view,
        name="post_comment",
    ),
    path(
        route="tag/<slug:tag_slug>/",
        view=views.post_list_view,
        name="post_list_by_tag",
    ),
    path(
        route="feed/",
        view=LatestPostsFeed(),
        name="post_feed",
    ),
    path(
        route="search/",
        view=views.post_search_view,
        name="post_search",
    ),
]
