from django.db import models
from products.models import Products
# Create your models here.
class Contacts(models.Model):
    title = models.CharField(blank=False, max_length=180, verbose_name='Наименование')
    text = models.CharField(blank=False, max_length=180, verbose_name='Текст (выводимый)')
    link = models.CharField(blank=False, max_length=180, verbose_name='Ссылка', help_text='Например https://t.me/link')
    code = models.CharField(blank=False, default='fa-phone', max_length=180, verbose_name='Код иконки', help_text='Например fa-shower https://fontawesome.com/v4/icon/question')
    show_in_top = models.BooleanField(default=False, verbose_name='Выводить сверху')
    show_in_bottom = models.BooleanField(default=False, verbose_name='Выводить снизу')
    ranc = models.IntegerField(blank=False, default=1, verbose_name='Порядок вывода')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['ranc']

    def __str__(self):
        return self.title
    
class Callrequest(models.Model):
    number = models.CharField(blank=False, null=False, max_length=80, verbose_name='Номер телефона')
    dateandtame = models.DateTimeField(blank=False, null=False, auto_now_add=True, verbose_name='Дата и время')
    product = models.CharField(blank=False, null=False, max_length=800, verbose_name='Товар')
    is_called = models.BooleanField(default=False, verbose_name='Запрос обработан')
    class Meta:
        verbose_name = 'Заказ обратного звонка'
        verbose_name_plural = 'Заказы обратного звонка'

    def __str__(self):
        return str(self.number)
    
class Pricerequest(models.Model):
    number = models.CharField(blank=False, null=False, max_length=80, verbose_name='Номер телефона')
    qwestion = models.TextField(blank=False, null=False, max_length=800, verbose_name='Комментарий')
    is_called = models.BooleanField(default=False, verbose_name='Запрос обработан')

    class Meta:
        verbose_name = 'Заказ оптового прайса'
        verbose_name_plural = 'Заказы оптового прайса'

    def __str__(self):
        return str(self.number)
    
class Holdmerequest(models.Model):
    number = models.CharField(blank=False, null=False, max_length=80, verbose_name='Номер телефона')
    dateandtame = models.DateTimeField(blank=False, null=False, auto_now_add=True, verbose_name='Дата и время')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар')
    is_called = models.BooleanField(default=False, verbose_name='Запрос обработан')
    class Meta:
        verbose_name = 'Просьба сообщить о поступлении'
        verbose_name_plural = 'Просьбы сообщить о поступлении'

    def __str__(self):
        return str(self.number)
    
    def get_first_product_image(self):
        """Возвращает первое изображение связанного продукта"""
        first_image = self.product.productimages.first()
        return first_image.image if first_image else None

class Fquestions(models.Model):
    question = models.TextField(blank=False, null=False, max_length=80, verbose_name='Вопрос')
    answer = models.TextField(blank=False, null=False, max_length=500, verbose_name='Ответ')
    ranc = models.IntegerField(blank=False, default=1, verbose_name='Порядок вывода')
    show = models.BooleanField(default=True, verbose_name='Выводить на странице')
    
    class Meta:
        verbose_name = 'Частый вопрос'
        verbose_name_plural = 'Частые вопросы'
        ordering = ['ranc']

    def __str__(self):
        return str(self.question)
    
class Slider(models.Model):
    text_min = models.TextField(blank=True, null=False, max_length=80, verbose_name='Мелкий текст')
    text_big = models.TextField(blank=True, null=False, max_length=500, verbose_name='Большой текст')
    text_button = models.CharField(blank=True, null=False, max_length=80, verbose_name='Текст кнопки')
    text_link = models.CharField(blank=True, null=False, max_length=500, verbose_name='Ссылка кнопки')
    image = models.ImageField(blank=False, upload_to='slider_images', verbose_name='Изображение фоновое', help_text='1980 на 748 пикселей')
    image_min = models.ImageField(blank=True, upload_to='slider_images', verbose_name='Изображение маленькое', help_text='406 на 404 пикселей')
    ranc = models.IntegerField(blank=False, default=1, verbose_name='Порядок вывода')
    show = models.BooleanField(default=True, verbose_name='Выводить на баннер?')
    
    class Meta:
        verbose_name = 'Слайд баннера на главной'
        verbose_name_plural = 'Слайды баннера на главной'
        ordering = ['ranc']

    def __str__(self):
        return str(self.text_big)
    










PAGES_TYPES = [
    ('delivery', 'доставка'),
    ('uslovija_vozvrata', 'условия возврата'),
    ('home', 'главная'),
]

IMAGE_SIDES = [
    ('left', 'слева'),
    ('right', 'справа'),
]

class Pages(models.Model):
    page = models.CharField(max_length=20, choices=PAGES_TYPES, verbose_name='Страница')
    title = models.CharField(blank=False, max_length=180, verbose_name='title')
    description = models.TextField(blank=False, null=False, max_length=500, verbose_name='description (описание страницы)') 
    span = models.TextField(blank=True, null=False, max_length=500, verbose_name='Заголовок верхний')
    h1 = models.TextField(blank=True, null=False, max_length=500, verbose_name='Заголовок главный')

    class Meta:
        verbose_name = 'Настройка страницы'
        verbose_name_plural = 'Настройки страниц'
    
    def __str__(self):
        return f"{self.get_page_display()} - {self.title}"
    
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
    page = models.ForeignKey(Pages, on_delete=models.CASCADE, verbose_name='Страница', related_name="%(class)s_blocks")
    ranc = models.IntegerField(blank=False, null=False, default=1, verbose_name='Порядок вывода')
    
    class Meta:
        abstract = True
        ordering = ['ranc']

    def get_block_type(self):
        """Определяет тип блока для шаблона"""
        if hasattr(self, 'image') and hasattr(self, 'text') and hasattr(self, 'side'):
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
    side = models.CharField(max_length=20, blank=False, null=False, default='right', choices=IMAGE_SIDES, verbose_name='Положение изображения')
    
    class Meta:
        verbose_name = 'Блок с текстом и изображением'
        verbose_name_plural = 'Блоки с текстом и изображением'
    
    def __str__(self):
        return f"Текст+Изображение {self.ranc}"

class VideoBlock(BaseBlock):
    h2 = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Заголовок')
    frame = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Код видео', help_text='Обязательно заменить на значения width="100%" height="400"')
    class Meta:
        verbose_name = 'Блок с видео'
        verbose_name_plural = 'Блоки с видео'
    
    def __str__(self):
        return f"Видео {self.ranc}"
# Контакты продвинутые
'''
from django.db import models
from django.utils.html import format_html
import re

class Contact(models.Model):
    
    CONTACT_TYPES = [
        ('phone', 'Телефон'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('address', 'Адрес'),
        ('worktime', 'Время работы'),
        ('email', 'Email'),
        ('vk', 'VKontakte'),
        ('instagram', 'Instagram'),
        ('other', 'Другое'),
    ]
    
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPES, verbose_name='Тип контакта', default='phone')
    value = models.CharField(max_length=255, verbose_name='Значение', help_text='Введите телефон, ссылку или текст')
    display_text = models.CharField(max_length=255, verbose_name='Текст для отображения', blank=True, help_text='Если оставить пустым, будет использовано значение')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок', help_text='Чем меньше число, тем выше в списке')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.get_contact_type_display()}: {self.value}"
    
    def clean_phone_number(self, phone):
        """Очистка номера телефона от лишних символов"""
        # Убираем все нецифровые символы, кроме плюса в начале
        cleaned = re.sub(r'[^\d+]', '', phone)
        return cleaned
    
    def get_icon(self):
        """Возвращает иконку Font Awesome в зависимости от типа"""
        icons = {
            'phone': 'fa-phone',
            'whatsapp': 'fa-whatsapp',
            'telegram': 'fa-telegram',
            'address': 'fa-home',
            'worktime': 'fa-clock-o',
            'email': 'fa-envelope',
            'vk': 'fa-vk',
            'instagram': 'fa-instagram',
            'other': 'fa-info-circle',
        }
        return icons.get(self.contact_type, 'fa-info-circle')
    
    def get_link(self):
        """Формирует ссылку в зависимости от типа контакта"""
        if not self.value:
            return ''
        
        display_text = self.display_text if self.display_text else self.value
        
        if self.contact_type == 'phone':
            cleaned_phone = self.clean_phone_number(self.value)
            return format_html(
                '<a href="tel:{phone}" style="color: black; padding-top: 20px;">'
                '<i class="fa {icon}" style="color: #0d6efd; font-size: 24px; padding-right: 10px;"></i>'
                '{text}</a>',
                phone=cleaned_phone,
                icon=self.get_icon(),
                text=display_text
            )
        
        elif self.contact_type == 'whatsapp':
            # Для WhatsApp ссылка должна быть в международном формате без плюса
            cleaned_phone = self.clean_phone_number(self.value)
            if cleaned_phone.startswith('+'):
                whatsapp_number = cleaned_phone[1:]  # Убираем плюс
            elif cleaned_phone.startswith('8') and len(cleaned_phone) == 11:
                whatsapp_number = '7' + cleaned_phone[1:]  # Заменяем 8 на 7
            else:
                whatsapp_number = cleaned_phone
            
            return format_html(
                '<a href="https://wa.me/{phone}" style="color: black; padding-top: 20px;" target="_blank">'
                '<i class="fa {icon}" style="color: #0d6efd; font-size: 24px; padding-right: 10px;"></i>'
                '{text}</a>',
                phone=whatsapp_number,
                icon=self.get_icon(),
                text=display_text
            )
        
        elif self.contact_type == 'telegram':
            # Если начинается с @, убираем его для ссылки
            if self.value.startswith('@'):
                username = self.value[1:]
            else:
                username = self.value
            
            return format_html(
                '<a href="https://t.me/{username}" style="color: black; padding-top: 20px;" target="_blank">'
                '<i class="fa {icon}" style="color: #0d6efd; font-size: 24px; padding-right: 10px;"></i>'
                '{text}</a>',
                username=username,
                icon=self.get_icon(),
                text=display_text
            )
        
        elif self.contact_type == 'email':
            return format_html(
                '<a href="mailto:{email}" style="color: black; padding-top: 20px;">'
                '<i class="fa {icon}" style="color: #0d6efd; font-size: 24px; padding-right: 10px;"></i>'
                '{text}</a>',
                email=self.value,
                icon=self.get_icon(),
                text=display_text
            )
        
        elif self.contact_type in ['vk', 'instagram']:
            # Для социальных сетей проверяем, есть ли https://
            link = self.value
            if not link.startswith(('http://', 'https://')):
                link = f'https://{link}'
            
            return format_html(
                '<a href="{link}" style="color: black; padding-top: 20px;" target="_blank">'
                '<i class="fa {icon}" style="color: #0d6efd; font-size: 24px; padding-right: 10px;"></i>'
                '{text}</a>',
                link=link,
                icon=self.get_icon(),
                text=display_text
            )
        
        else:  # address, worktime, other
            return format_html(
                '<div style="color: black; padding-top: 20px;">'
                '<i class="fa {icon}" style="color: #0d6efd; font-size: 24px; padding-right: 10px;"></i>'
                '{text}</div>',
                icon=self.get_icon(),
                text=display_text
            )
    
    def get_link_html(self):
        """Безопасный вывод HTML"""
        return self.get_link()
    get_link_html.allow_tags = True
    get_link_html.short_description = 'Предпросмотр'
'''

