from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path(route="", view=views.post_list_view, name="post_list"),
    path(route="<int:id>/", view=views.post_detail_view, name="post_detail"),
]
