from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    slug = models.SlugField(blank=False, null=False, max_length=200, unique=True, verbose_name='slug для url')
    title = models.CharField(blank=False, max_length=180, verbose_name='title')
    image = models.ImageField(blank=False, upload_to='articles', verbose_name='Изображение карточки')
    about = models.TextField(blank=True, null=True, max_length=1500, verbose_name='Краткое описание')
    description = models.TextField(blank=False, null=False, max_length=500, verbose_name='description (описание страницы)') 
    span = models.TextField(blank=True, null=False, max_length=500, verbose_name='Заголовок верхний')
    h1 = models.TextField(blank=True, null=False, max_length=500, verbose_name='Заголовок главный')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("articlesapp:articledetail", kwargs={"slug": self.slug})
    
    def get_all_blocks_sorted(self):
        """Получить ВСЕ блоки страницы, отсортированные по ranc"""
        # Собираем все блоки в один список
        blocks = []
        blocks.extend(list(self.imageblock_blocks.all()))
        blocks.extend(list(self.textblock_blocks.all()))
        blocks.extend(list(self.imagetextblock_blocks.all()))
        blocks.extend(list(self.videoblock_blocks.all()))
        
        # Сортируем по полю ranc
        return sorted(blocks, key=lambda x: x.ranc)
    
    def get_blocks_grouped_sorted(self):
        """Получить блоки сгруппированные по типу и отсортированные внутри групп"""
        return {
            'image_blocks': self.imageblock_blocks.all(),
            'text_blocks': self.textblock_blocks.all(),
            'image_text_blocks': self.imagetextblock_blocks.all(),
            'video_blocks': self.videoblock_blocks.all(),
        }

class BaseBlock(models.Model):
    page = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name="%(class)s_blocks")
    ranc = models.IntegerField(blank=False, null=False, default=1, verbose_name='Порядок вывода')
    
    class Meta:
        abstract = True
        ordering = ['ranc']

    def get_block_type(self):
        """Определяет тип блока для шаблона"""
        if hasattr(self, 'image') and hasattr(self, 'text'):
            return 'ImageTextBlock'
        elif hasattr(self, 'frame'):
            return 'VideoBlock'
        elif hasattr(self, 'image'):
            return 'ImageBlock'
        elif hasattr(self, 'text'):
            return 'TextBlock'
        return 'Unknown'

class ImageBlock(BaseBlock):
    image = models.ImageField(blank=True, upload_to='pagesimages', verbose_name='Изображение', help_text='750px X 495px')
    alt = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Небольшое описание изображения для СЕО')
    class Meta:
        verbose_name = 'Блок с изображением'
        verbose_name_plural = 'Блоки с изображением'
    
    def __str__(self):
        return f"Изображение {self.ranc}"

class TextBlock(BaseBlock):
    h2 = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Заголовок')
    text = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Текст')
    
    class Meta:
        verbose_name = 'Блок с текстом'
        verbose_name_plural = 'Блоки с текстом'
    
    def __str__(self):
        return f"Текст {self.ranc}"

class ImageTextBlock(BaseBlock):
    h2 = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Заголовок')
    text = models.TextField(blank=False, null=False, max_length=2500, verbose_name='Текст')
    image = models.ImageField(blank=False, upload_to='pagesimages', verbose_name='Изображение', help_text='370px X 400px')
    alt = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Небольшое описание изображения для СЕО')
    
    class Meta:
        verbose_name = 'Блок с текстом и изображением'
        verbose_name_plural = 'Блоки с текстом и изображением'
    
    def __str__(self):
        return f"Текст+Изображение {self.ranc}"

class VideoBlock(BaseBlock):
    h2 = models.CharField(blank=True, null=True, max_length=2500, verbose_name='Заголовок')
    frame = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Код видео', help_text='Обязательно заменить на значения width="100%" height="400"')
    class Meta:
        verbose_name = 'Блок с видео'
        verbose_name_plural = 'Блоки с видео'
    
    def __str__(self):
        return f"Видео {self.ranc}"