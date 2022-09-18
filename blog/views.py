from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


# def post_list_view(request):
#     post_list = Post.published.all()

#     paginator = Paginator(post_list, per_page=3)
#     page_number = request.GET.get("page", 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     return render(
#         request=request,
#         template_name="blog/post/list.html",
#         context={"posts": posts},
#     )


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


def post_share_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends You to read {post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=cd["email"],
                recipient_list=[cd["to"]],
            )
            sent = True
    else:
        form = EmailPostForm()

    return render(
        request=request,
        template_name="blog/post/share.html",
        context={"post": post, "form": form, "sent": sent},
    )
