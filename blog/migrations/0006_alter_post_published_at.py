# Generated by Django 4.1.1 on 2022-09-19 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_tags_alter_post_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 9, 19, 8, 44, 57, 897168, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
