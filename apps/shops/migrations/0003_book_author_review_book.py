# Generated by Django 5.1.2 on 2024-10-16 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0002_book_country_review"),
        ("users", "0002_author_remove_user_first_name_remove_user_last_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(to="users.author"),
        ),
        migrations.AddField(
            model_name="review",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="shops.book",
            ),
        ),
    ]
