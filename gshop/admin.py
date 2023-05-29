from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import User

from .models import Product, Category, Promotion
from .utils import EMailThread


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'photo', 'is_available')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'category')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        if obj.send_now:
            users = User.objects.all()
            for user in users:
                thread = EMailThread(user.email, request.POST['title'], request.POST['text'])
                thread.run()
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Promotion, PromotionAdmin)
