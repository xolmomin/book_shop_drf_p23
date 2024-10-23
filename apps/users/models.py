from django.contrib.auth.models import AbstractUser
from django.db.models import Model, EmailField, CharField, CASCADE, TextField, Model, ForeignKey, PositiveIntegerField, \
    RESTRICT, ManyToManyField, BooleanField, OneToOneField
from mptt.models import MPTTModel

from shared.models import TimeBasedModel
from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = EmailField(unique=True)
    name = CharField(max_length=255)
    is_active = BooleanField(default=False)
    shipping_address = OneToOneField('users.Address', RESTRICT, null=True, blank=True, related_name='shipping_user')
    billing_address = OneToOneField('users.Address', RESTRICT, null=True, blank=True, related_name='billing_user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    wishlist = ManyToManyField('shops.Book', blank=True, related_name='wishlist')


class Author(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    description = TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Address(TimeBasedModel):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    address_line_1 = CharField(max_length=255)
    address_line_2 = CharField(max_length=255, null=True, blank=True)
    city = CharField(max_length=255)
    state = CharField(max_length=255, null=True, blank=True)
    postal_code = PositiveIntegerField(db_default=0, null=True, blank=True)
    phone_number = CharField(max_length=16)  # todo + siz saqlash kerak
    country = ForeignKey('users.Country', CASCADE)
    user = ForeignKey('users.User', RESTRICT)

    # def clean(self):
    #     if self.phone_number and not self.phone_number.startswith('+'):
    #         self.phone_number = self.phone_number.removeprefix('+')
    #     if len(self.phone_number) < 16:
    #         raise ValidationError('Telefon raqami to\'g\'ri emas.')

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Cart(TimeBasedModel):
    book = ForeignKey('shops.Book', CASCADE)
    owner = ForeignKey('users.User', CASCADE)
    quantity = PositiveIntegerField(db_default=1)
    '''
    format
    condition
    seller
    ship from
    '''

    def __str__(self):
        return f"{self.owner} - {self.book}"


class Country(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name
