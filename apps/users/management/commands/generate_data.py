from datetime import UTC

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from faker.proxy import Faker

from shops.models import Book, Section, Review, Category
from users.models import User, Author, Address, Country, Cart


class Command(BaseCommand):
    model_list = {'user', 'author', 'address', 'book', 'section', 'cart', 'review', 'category'}

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        self.f = Faker()
        super().__init__(stdout, stderr, no_color, force_color)

    def add_arguments(self, parser):
        for model in self.model_list:
            parser.add_argument(f'--{model}', type=int, default=0)

    def _book(self):
        return Book(
            slug=self.f.slug(),
            overview=self.f.paragraph(),
            features=self.f.json(),
            format=self.f.random_element(elements=[Book.Format.HARD_COVER, Book.Format.PAPER_COVER]),
            used_good_price=self.f.pydecimal(left_digits=4, right_digits=2, positive=True),
            new_price=self.f.pydecimal(left_digits=4, right_digits=2, positive=True),
            ebook_price=self.f.pydecimal(left_digits=4, right_digits=2, positive=True),
            audiobook_price=self.f.pydecimal(left_digits=4, right_digits=2, positive=True),
            reviews_count=self.f.random_int(min=0, max=100)
        )

    def _user(self):
        return User(
            email=self.f.email(domain='gmail.com'),
            name=self.f.name(),
            is_active=self.f.boolean(),
            password=make_password(self.f.password()),
            date_joined=self.f.date_time(tzinfo=UTC),
        )

    def _address(self):
        return Address(
            first_name=self.f.first_name(),
            last_name=self.f.last_name(),
            address_line_1=self.f.address(),
            address_line_2=self.f.address(),
            city=self.f.city(),
            state=self.f.state(),
            postal_code=self.f.postalcode(),
            country_id=Country.objects.order_by('?').values_list('id', flat=True).first(),
            user_id=User.objects.order_by('?').values_list('id', flat=True).first(),
        )

    def _section(self):
        return Section(
            name_image=self.f.image_url(),
            intro=self.f.text(),
            banner=self.f.image_url(),
        )

    def _cart(self):
        return Cart(
            book_id=Book.objects.order_by('?').values_list('id', flat=True).first(),
            owner_id=User.objects.order_by('?').values_list('id', flat=True).first(),
            quantity=self.f.random_int(min=1, max=100),
        )

    def _review(self):
        return Review(
            name=self.f.name(),
            description=self.f.text(),
            stars=self.f.random_int(min=1, max=10),
            book_id=Book.objects.order_by('?').values_list('id', flat=True).first()
        )

    def _author(self):
        return Author(
            first_name=self.f.first_name(),
            last_name=self.f.last_name(),
            description=self.f.text()
        )

    def _category(self):
        return Category.objects.insert_node(
            Category(
                name=self.f.word(),
                parent_id=Category.objects.order_by('?').values_list('id', flat=True).first(),
                section_id=Section.objects.order_by('?').values_list('id', flat=True).first()
            ),
            None
        )

    def _generate_object(self, cls, name, count=0):
        cls.objects.bulk_create([getattr(self, f'_{name}')() for _ in range(count)])
        self.stdout.write(self.style.SUCCESS(f"{cls.__name__} malumotlari {count} tadan qo'shildi"))

    def handle(self, *args, **options):
        _models = globals()
        for name in self.model_list & set(options):
            if options[name]:
                self._generate_object(_models[name.capitalize()], name, options[name])

        self.stdout.write(self.style.SUCCESS(f"Barcha malumotlar qo'shildi"))
