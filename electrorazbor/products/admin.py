from django.contrib import admin
from .models import Categories, Products, ProductsImages, CharacteristicsMiddleModel, Characteristics
# Register your models here.

class CharacteristicsMiddleModelInline(admin.StackedInline):
    model = CharacteristicsMiddleModel

class ProductsImagesInline(admin.StackedInline):
    model = ProductsImages

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "in_top",)
    list_editable = ("in_top",)
    list_filter = ("category",)
    filter_horizontal = ("category",) #для удобного добавления
    prepopulated_fields = {"slug": ("name", )}
    inlines =(CharacteristicsMiddleModelInline, ProductsImagesInline,)


@admin.register(Characteristics)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ("name",)