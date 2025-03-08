from django.contrib import admin
from product.models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "category", "description", "price", "photo", "slug")

