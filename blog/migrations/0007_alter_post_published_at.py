# Generated by Django 4.1.1 on 2022-09-19 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_post_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 9, 19, 9, 58, 11, 543168, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
