from django.contrib import admin
from .models import Article, TextBlock, ImageBlock, ImageTextBlock, VideoBlock


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

class ImageTextBlockInline(admin.StackedInline):
    model = ImageTextBlock
    extra = 1
    verbose_name = "Блок с текстом и изображением"
    verbose_name_plural = "Блоки с текстом и изображением"

class VideoBlockInline(admin.StackedInline):
    model = VideoBlock
    extra = 1
    verbose_name = "Видео блок"
    verbose_name_plural = "Видео блоки"

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "blocks_count")
    search_fields = ("title", "description", "h1")
    prepopulated_fields = {"slug": ("title", )}
    # Группируем инлайны
    inlines = [TextBlockInline, ImageBlockInline, ImageTextBlockInline, VideoBlockInline]
    
    def blocks_count(self, obj):
        """Показывает общее количество блоков на странице"""
        # через related_name
        total = 0
        total += obj.imageblock_blocks.count() if hasattr(obj, 'imageblock_blocks') else 0
        total += obj.textblock_blocks.count() if hasattr(obj, 'textblock_blocks') else 0
        total += obj.imagetextblock_blocks.count() if hasattr(obj, 'imagetextblock_blocks') else 0
        total += obj.videoblock_blocks.count() if hasattr(obj, 'videoblock_blocks') else 0
        return total
    
    blocks_count.short_description = "Всего блоков"
    
    fieldsets = (
        ('Мета-информация', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Заголовки страницы', {
            'fields': ('span', 'h1', 'image', 'about'),
            'classes': ('wide',)
        }),
    )