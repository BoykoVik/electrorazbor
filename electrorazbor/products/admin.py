from django.contrib import admin
from .models import Categories, Products, ProductsImages
# Register your models here.

class ProductsImagesInline(admin.StackedInline):
    model = ProductsImages

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_filter = ("category",)
    filter_horizontal = ("category",) #для удобного добавления
    prepopulated_fields = {"slug": ("name", )}
    inlines =(ProductsImagesInline,)