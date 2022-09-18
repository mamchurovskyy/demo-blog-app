from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list_view(request):
    posts = Post.published.all()
    return render(
        request=request,
        template_name="blog/post/list.html",
        context={"posts": posts},
    )


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
    )

    return render(
        request=request,
        template_name="blog/post/detail.html",
        context={"post": post},
    )
