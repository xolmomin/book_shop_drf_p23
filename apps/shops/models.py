from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField, CASCADE, TextField, ImageField, Model, ForeignKey, JSONField, TextChoices, \
    DecimalField, PositiveIntegerField, PositiveSmallIntegerField, ManyToManyField
from mptt.models import MPTTModel, TreeForeignKey

from shared.models import TimeBasedModel, SlugTimeBasedModel


class Section(TimeBasedModel):
    name_image = ImageField(upload_to='shops/categories/name_image/%Y/%m/%d', null=True, blank=True)
    intro = TextField(null=True, blank=True)
    banner = ImageField(upload_to='shops/categories/banner/%Y/%m/%d', null=True, blank=True)


class Category(MPTTModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='subcategories')
    section = ForeignKey('shops.Section', CASCADE, null=True, blank=True, related_name='categories')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class MPTTMeta:
        order_insertion_by = ['name']


class Book(SlugTimeBasedModel):
    class Format(TextChoices):
        HARD_COVER = 'hard_cover', 'Hard cover'
        PAPER_COVER = 'paper_cover', 'Paper cover'

    overview = TextField()
    features = JSONField()
    # format = CharField(max_length=255, choices=Format, default=Format.HARDCOVER) # todo togirlash kerak buni
    used_good_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    new_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ebook_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    audiobook_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    author = ManyToManyField('users.Author')
    reviews_count = PositiveIntegerField(db_default=0)


class Review(TimeBasedModel):
    name = CharField(max_length=255)
    description = TextField()
    stars = PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    book = ForeignKey('shops.Book', CASCADE, related_name='reviews')

    def __str__(self):
        return self.name

    @property
    def star(self):
        return self.stars / 2
