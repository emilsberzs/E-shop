from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin  # pylint: disable=import-error


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'available', 'price', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']

    def get_prepolopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
