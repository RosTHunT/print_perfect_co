from django.contrib import admin

from app_product.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'recommended', 'updated_at', 'created_at')
    list_display_links = ('pk', 'title')
    readonly_fields = ('updated_at', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'price_last', 'quantity', 'is_published')
    list_display_links = ('pk', 'title')
    readonly_fields = ('uploaded_at', 'updated_at', 'created_at')
