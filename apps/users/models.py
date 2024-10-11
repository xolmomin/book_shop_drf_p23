from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField, CASCADE, ForeignKey


class User(AbstractUser):
    pass
    # wishlist = ManyToManyField('shops.Book', CASCADE, blank=True)
