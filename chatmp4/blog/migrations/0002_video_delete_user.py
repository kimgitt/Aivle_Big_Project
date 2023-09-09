# Generated by Django 4.2 on 2023-06-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                ("video_id", models.AutoField(primary_key=True, serialize=False)),
                ("video_title", models.CharField(max_length=30)),
                ("video_addr", models.CharField(max_length=50)),
                ("upload_date", models.DateTimeField()),
            ],
            options={
                "db_table": "video",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
