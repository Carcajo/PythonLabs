from django.conf.urls.static import static
from django.urls import path

from lab3 import settings
from orders.views import order_create

urlpatterns = [
    path('checkout/', order_create, name='checkout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
