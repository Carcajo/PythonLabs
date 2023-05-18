from django.db import models
from django.urls import reverse


# from django.utils.translation import gettext as translated


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product name")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Unique Identifier", unique=True)
    description = models.TextField(verbose_name="Product Description")
    price = models.FloatField(verbose_name="Price")
    photo = models.ImageField(upload_to=f"photos/", verbose_name="Picture")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    is_available = models.BooleanField(default=True, verbose_name="In stock")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={"product_slug": self.slug, "category_slug": self.category.slug})

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=180, db_index=True, verbose_name="Product type")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Unique Identifier", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Product type"
        verbose_name_plural = "Product types"
        ordering = ['name']


class Promotion(models.Model):
    title = models.CharField(max_length=180, verbose_name="Share name")
    text = models.TextField(verbose_name="Text")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Publication time")
    send_now = models.BooleanField(default=True, verbose_name="Send email to all buyers")

    class Meta:
        verbose_name = "Special offer"
        verbose_name_plural = "Special offers"
        ordering = ['time_create']
