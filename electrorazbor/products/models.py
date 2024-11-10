from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    name = models.CharField(blank=False, max_length=350, verbose_name='Наименование категории товара')
    slug = models.SlugField(blank=False, null=False, max_length=200, unique=True, verbose_name='slug для url')
    desctiption = models.TextField(blank=True, null=True, max_length=500, verbose_name='description (описание страницы)')


    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:products_category", kwargs={"slug": self.slug})
    

class Products(models.Model):
    name = models.CharField(blank=False, max_length=350, verbose_name='Наименование')
    about = models.TextField(blank=True, null=True, max_length=1500, verbose_name='Краткое описание')
    about_big = models.TextField(blank=True, null=True, max_length=2500, verbose_name='Большое описание')
    price = models.IntegerField(blank=False, null=False, default=100, verbose_name='Цена')
    in_top = models.BooleanField(default=False, verbose_name='В топе')
    desctiption = models.TextField(blank=False, null=False, max_length=500, verbose_name='description (описание страницы)')
    slug = models.SlugField(blank=True, null=True, max_length=200, unique=True, verbose_name='slug для url')
    category = models.ManyToManyField(Categories, blank=False, verbose_name='Вид товара', related_name='category')
    show = models.BooleanField(default=True, verbose_name='В наличии?')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:productdetail", kwargs={"slug": self.slug})
    

class ProductsImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар', related_name="productimages")
    image = models.ImageField(blank=True, upload_to='productsimages', verbose_name='Изображение')
    
    def __str__(self):
        return self.product.name
        
    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'
        ordering = ['id']


class Characteristics(models.Model):# ХАРАКТЕРИСТИКИ
    name = models.CharField(blank=False, max_length=350, unique=True, verbose_name='Наименование характеристики')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
class CharacteristicsMiddleModel(models.Model):# ПРОМЕЖУТОЧНАЯ МОДЕЛЬ
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL, related_name='product', verbose_name='Товар')
    characteristic = models.ForeignKey(Characteristics, null=True, on_delete=models.SET_NULL, verbose_name='Характеристика')
    count = models.CharField(blank=True, null=True, max_length=1500, verbose_name='Показатель')

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'
        ordering = ['id']