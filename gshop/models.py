from django.db import models
from django.urls import reverse


# from django.utils.translation import gettext as translated


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование продукта")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", unique=True)
    description = models.TextField(verbose_name="Описание продукта")
    price = models.FloatField(verbose_name="Цена")
    photo = models.ImageField(upload_to=f"photos/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={"product_slug": self.slug, "category_slug": self.category.slug})

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=180, db_index=True, verbose_name="Тип продукта")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"
        ordering = ['name']


class Promotion(models.Model):
    title = models.CharField(max_length=180, verbose_name="Название акции")
    text = models.TextField(verbose_name="Текст")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")
    send_now = models.BooleanField(default=True, verbose_name="Отправить email всем покупателям")

    class Meta:
        verbose_name = "Специальное предложение"
        verbose_name_plural = "Специальные предложения"
        ordering = ['time_create']

# Create your models here.

# mail password: 1JQ4nSiorAGojyHRpKzv
