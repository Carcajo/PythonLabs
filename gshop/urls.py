from django.urls import path

from .views import index, about, AllProducts, RegisterUser, CatProducts, UnoProduct, LoginUser, logout_user

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('products/', AllProducts.as_view(), name="all_products"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('<slug:category_slug>/', CatProducts.as_view(), name="category"),
    path('<slug:category_slug>/<slug:product_slug>/', UnoProduct.as_view(), name="product")
]
