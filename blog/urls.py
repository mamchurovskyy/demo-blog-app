from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path(route="", view=views.post_list_view, name="post_list"),
    # SEO-friendly URL
    path(
        route="<int:year>/<int:month>/<int:day>/<slug:post>/",
        view=views.post_detail_view,
        name="post_detail",
    ),
]
