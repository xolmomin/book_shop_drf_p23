# Generated by Django 5.1.2 on 2024-10-16 12:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0003_book_author_review_book"),
        ("users", "0003_country_alter_address_country"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Country",
        ),
    ]
