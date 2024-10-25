from django.db import models

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