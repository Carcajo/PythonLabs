import rest_framework.status as status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import Category, Product


class TestViewsModels(APITestCase):
    def test_home_get(self):
        url = reverse_lazy("home")
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_all_products_get(self):
        url = reverse_lazy("all_products")
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_about_get(self):
        url = reverse_lazy("about")
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_login_get(self):
        url = reverse_lazy("login")
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_logout_get(self):
        url = reverse_lazy("logout")
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_register_get(self):
        url = reverse_lazy("register")
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_cat_empty_get(self):
        category_slug = "food"
        url = reverse_lazy("category", args=(category_slug,))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_404_NOT_FOUND, code)

    def test_product_not_empty_get(self):
        cat = Category.objects.create(name="food", slug="dinner")
        prod = Product.objects.create(
            name="pasta",
            slug="karbonara",
            description="test",
            price=123.0,
            category=cat,
        )
        url = reverse_lazy("product", args=(cat.slug, prod.slug))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_register_post(self):
        url = reverse_lazy("register")
        code = self.client.post(
            url,
            {
                "username": "carcajo",
                "first_name": "maxim",
                "last_name": "puhov",
                "phone_number": "+375445391507",
                "mail": "t375445391507@gmail.com",
                "password1": "pass1234",
            },
        ).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_login_post(self):
        url = reverse_lazy("login")
        User.objects.create_user({"username": "user", "password": "pass1234"})
        code = self.client.post(
            url, {"username": "user", "password": "pass1234"}
        ).status_code
        self.assertEqual(status.HTTP_200_OK, code)
