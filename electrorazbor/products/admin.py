from django.contrib import admin
from .models import Categories, Products, ProductsImages, CharacteristicsMiddleModel, Characteristics, Firms, Obtains, Orders
from django.utils.safestring import mark_safe
# Register your models here.

class CharacteristicsMiddleModelInline(admin.StackedInline):
    model = CharacteristicsMiddleModel

class ProductsImagesInline(admin.StackedInline):
    model = ProductsImages
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" style="object-fit: cover;" />')
        return "Нет изображения"
    image_preview.short_description = "Превью"
    
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
    list_display = ("id", "name", "price", "get_main_image", "in_top", "show", "rang", "use_in_feed",)
    list_editable = ("price", "in_top", "show", "rang", "use_in_feed",)
    list_filter = ("category", "show",)
    filter_horizontal = ("category", "like_what",) #для удобного добавления
    prepopulated_fields = {"slug": ("name", )}
    inlines =(CharacteristicsMiddleModelInline, ProductsImagesInline,)

    def get_main_image(self, obj):
        main_image = obj.productimages.first()
        if main_image:
            return mark_safe(f'<img src="{main_image.image.url}" width="50">')
        return "Нет фото"
    get_main_image.short_description = "Фото"


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