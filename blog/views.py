# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list_view(request):
    posts = Post.published.all()
    return render(
        request=request,
        template_name="blog/post/list.html",
        context={"posts": posts},
    )


def post_detail_view(request, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("The specified post was not found.")
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    return render(
        request=request,
        template_name="blog/post/detail.html",
        context={"post": post},
    )
