from django.db.models import Model, DateTimeField, CharField, BooleanField
from django.utils.text import slugify


class DeleteBasedModel(Model):
    is_deleted = BooleanField(db_default=False)

    class Meta:
        abstract = True


class TimeBasedModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugBasedModel(Model):
    title = CharField(max_length=255)
    slug = CharField(max_length=255, unique=True, editable=False)
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugTimeBasedModel(TimeBasedModel, SlugBasedModel):
    class Meta:
        abstract = True
