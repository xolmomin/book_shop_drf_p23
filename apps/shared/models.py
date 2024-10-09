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
    slug = CharField(max_length=255, unique=True)
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.slug is None:
            slug = slugify(self.title)
            if self.__class__.objects.filter(slug=slug).exists():
                self.slug += '-1'

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    class Meta:
        abstract = True


class SlugTimeBasedModel(TimeBasedModel, SlugBasedModel):
    class Meta:
        abstract = True
