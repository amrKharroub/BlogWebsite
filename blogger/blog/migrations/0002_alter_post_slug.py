# Generated by Django 4.2.5 on 2023-09-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
