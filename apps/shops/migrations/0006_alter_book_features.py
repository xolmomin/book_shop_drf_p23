# Generated by Django 5.1.2 on 2024-10-23 10:49

import django_jsonform.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0005_book_image_alter_book_audiobook_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="features",
            field=django_jsonform.models.fields.JSONField(),
        ),
    ]