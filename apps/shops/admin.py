from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import DraggableMPTTAdmin

from shops.models import Category, Book, Section


@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Book)
class BookModelAdmin(ModelAdmin):
    list_display = ['slug', 'title']
    autocomplete_fields = ['author']


@admin.register(Section)
class SectionModelAdmin(ModelAdmin):
    pass
