from django.contrib import admin
from .models import Categories, Products, ProductsImages, CharacteristicsMiddleModel, Characteristics, Firms, Obtains, Orders
# Register your models here.

class CharacteristicsMiddleModelInline(admin.StackedInline):
    model = CharacteristicsMiddleModel

class ProductsImagesInline(admin.StackedInline):
    model = ProductsImages

@admin.register(Firms)
class FirmsAdmin(admin.ModelAdmin):
    list_display = ("name", "rang",)
    list_editable = ("rang",)
    prepopulated_fields = {"slug": ("name", )}
    #filter_horizontal = ("category",) #для удобного добавления

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "firm",)
    list_editable = ("firm",)
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "in_top", "show", "rang", "use_in_feed",)
    list_editable = ("price", "in_top", "show", "rang", "use_in_feed",)
    list_filter = ("category", "show",)
    filter_horizontal = ("category",) #для удобного добавления
    prepopulated_fields = {"slug": ("name", )}
    inlines =(CharacteristicsMiddleModelInline, ProductsImagesInline,)


@admin.register(Characteristics)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ObtainsInline(admin.StackedInline):
    model = Obtains

@admin.register(Obtains)
class ObtainsAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "count",)
    list_filter = ("order",)
    search_fields = ("order",)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "phone",)
    list_filter = ("phone",)
    search_fields = ("phone", "date",)
    inlines =(ObtainsInline,)