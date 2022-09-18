from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class PublishedStatusManager(models.Manager):
    """Custom manager to retrieve all posts that have `PUBLISHED` status"""

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Data model for blog posts"""

    class Status(models.TextChoices):
        """Available choices for post status"""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        ordering = ("-published_at",)
        indexes = [
            # B-tree index in descending order
            models.Index(fields=("-published_at",))
        ]

    def __str__(self) -> str:
        return self.title
