# Generated by Django 4.1.1 on 2022-09-18 16:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_published_at_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 9, 18, 16, 31, 21, 18317, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("email", models.EmailField(max_length=254)),
                ("body", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
            },
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["created_at"], name="blog_commen_created_4e025c_idx"
            ),
        ),
    ]
