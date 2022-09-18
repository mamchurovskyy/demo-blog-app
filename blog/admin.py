from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Representation of the `Post` model in the admin interface"""

    list_display = [
        "title",
        "author",
        "published_at",
        "status",
    ]
    list_filter = [
        "status",
        "created_at",
        "published_at",
        "author",
    ]
    search_fields = [
        "title",
        "body",
    ]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "published_at"
    ordering = [
        "status",
        "published_at",
    ]
