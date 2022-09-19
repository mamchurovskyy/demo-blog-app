from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from taggit.models import Tag

from .forms import CommentForm, EmailPostForm, SearchForm
from .models import Comment, Post


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = "posts"
#     paginate_by = 3
#     template_name = "blog/post/list.html"


def post_list_view(request, tag_slug=None):
    post_list = Post.published.all()

    tag = None
    if tag_slug is not None:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, per_page=3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request=request,
        template_name="blog/post/list.html",
        context={"posts": posts, "tag": tag},
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
    comments = post.comments.filter(active=True)
    form = CommentForm()

    # Get IDs for the tags of the current post
    post_tags_ids = post.tags.values_list("id", flat=True)
    # Get all published posts that have any of these IDs,
    # the current post is excluded
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
        id=post.id
    )
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-published_at"
    )[:5]

    return render(
        request=request,
        template_name="blog/post/detail.html",
        context={
            "post": post,
            "comments": comments,
            "form": form,
            "similar_posts": similar_posts,
        },
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


@require_POST
def post_comment_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request=request,
        template_name="blog/post/comment.html",
        context={"post": post, "form": form, "comment": comment},
    )


def post_search_view(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Post.published.annotate(
                search=SearchVector("title", "body")
            ).filter(search=query)

    return render(
        request=request,
        template_name="blog/post/search.html",
        context={"form": form, "query": query, "results": results},
    )
