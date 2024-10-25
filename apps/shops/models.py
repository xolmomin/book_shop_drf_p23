from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField, CASCADE, TextField, ImageField, Model, ForeignKey, TextChoices, \
    DecimalField, PositiveIntegerField, PositiveSmallIntegerField, ManyToManyField
from django.utils.text import slugify
from django_jsonform.models.fields import JSONField
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

    SCHEMA = {
        'type': 'dict',  # or 'object'
        'keys': {  # or 'properties'
            'format': {
                'type': 'string',
                'title': 'Format'
            },
            'publisher': {
                'type': 'string',
                'title': 'Publisher',
            },
            'pages': {
                'type': 'integer',
                'title': 'Pages',
                'helpText': '(Optional)'
            },
            'dimensions': {
                'type': 'string',
                'title': 'Dimensions',
                'helpText': 'exp. 6.30 x 9.20 x 1.20 inches'
            },
            'shipping_weight': {
                'type': 'number',
                'title': 'Shipping Weight',
                'helpText': 'lbs'
            },
            'languages': {
                'type': 'string',
                'title': 'Language'
            },
            'publication_date': {
                'type': 'string',
                'title': 'Publication Date'
            },
            'isbn_13': {
                'type': 'integer',
                'title': 'ISBN-13'
            },
            'isbn_10': {
                'type': 'integer',
                'title': 'ISBN-10'
            },
            'edition': {
                'type': 'integer',
                'title': 'Edition',
                'helpText': '(Optional)'
            },
        },
        'required': ['format', 'languages', 'isbn_13', 'isbn_10', 'shipping_weight', 'dimensions', 'publication_date']
    }

    overview = TextField()
    features = JSONField(schema=SCHEMA)

    # format = CharField(max_length=255, choices=Format, default=Format.HARDCOVER) # todo togirlash kerak buni
    used_good_price = DecimalField(help_text='USD da kiritamiz', max_digits=6, decimal_places=2, blank=True, null=True)
    new_price = DecimalField(help_text='USD da kiritamiz', max_digits=6, decimal_places=2, blank=True, null=True)
    ebook_price = DecimalField(help_text='USD da kiritamiz', max_digits=6, decimal_places=2, blank=True, null=True)
    audiobook_price = DecimalField(help_text='USD da kiritamiz', max_digits=6, decimal_places=2, blank=True, null=True)
    author = ManyToManyField('users.Author', blank=True)
    image = ImageField(upload_to='shops/books/%Y/%m/%d')
    reviews_count = PositiveIntegerField(db_default=0, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = f"{slugify(self.title)}"

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)


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
