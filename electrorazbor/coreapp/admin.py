from django.contrib import admin
from .models import Contacts, Callrequest, Pricerequest, Fquestions, Slider, Pages, TextBlock, ImageBlock, ImageTextBlock, VideoBlock
# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("title", "ranc", "show_in_top", "show_in_bottom",)
    list_editable = ("ranc", "show_in_top", "show_in_bottom",)

@admin.register(Callrequest)
class CallrequestAdmin(admin.ModelAdmin):
    list_display = ("number", "dateandtame",)

@admin.register(Pricerequest)
class PricerequestAdmin(admin.ModelAdmin):
    list_display = ("number", "qwestion",)

@admin.register(Fquestions)
class FquestionsAdmin(admin.ModelAdmin):
    list_display = ("question", "ranc", "show",)
    list_editable = ("ranc", "show",)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("text_min", "id", "ranc", "show",)
    list_editable = ("ranc", "show",)

class ImageBlockInline(admin.TabularInline):
    model = ImageBlock
    extra = 1
    verbose_name = "Блок с изображением"
    verbose_name_plural = "Блоки с изображениями"

class TextBlockInline(admin.TabularInline):
    model = TextBlock
    extra = 1
    verbose_name = "Текстовый блок"
    verbose_name_plural = "Текстовые блоки"

class ImageTextBlockInline(admin.TabularInline):
    model = ImageTextBlock
    extra = 1
    verbose_name = "Блок с текстом и изображением"
    verbose_name_plural = "Блоки с текстом и изображением"

class VideoBlockInline(admin.TabularInline):
    model = VideoBlock
    extra = 1
    verbose_name = "Видео блок"
    verbose_name_plural = "Видео блоки"

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "blocks_count")
    list_filter = ("page",)
    search_fields = ("title", "description", "h1")
    
    # Группируем инлайны
    inlines = [TextBlockInline, ImageBlockInline, ImageTextBlockInline, VideoBlockInline]
    
    def blocks_count(self, obj):
        """Показывает общее количество блоков на странице"""
        # Используйте правильные related_name
        total = 0
        # imageblock_blocks вместо imageblock_set
        total += obj.imageblock_blocks.count() if hasattr(obj, 'imageblock_blocks') else 0
        # textblock_blocks вместо textblock_set
        total += obj.textblock_blocks.count() if hasattr(obj, 'textblock_blocks') else 0
        # imagetextblock_blocks вместо imagetextblock_set
        total += obj.imagetextblock_blocks.count() if hasattr(obj, 'imagetextblock_blocks') else 0
        # videoblock_blocks вместо videoblock_set
        total += obj.videoblock_blocks.count() if hasattr(obj, 'videoblock_blocks') else 0
        return total
    
    blocks_count.short_description = "Всего блоков"
    
    fieldsets = (
        ('Мета-информация', {
            'fields': ('page', 'title', 'description')
        }),
        ('Заголовки страницы', {
            'fields': ('span', 'h1'),
            'classes': ('wide',)
        }),
    )