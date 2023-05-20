import rest_framework.status as status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from gshop.models import Category, Product


class TestCart(APITestCase):
    def test_cart_add_no_login_post(self):
        food = Category.objects.create(name="food", slug="dinner")
        prod = Product.objects.create(
            name="pasta",
            slug="karbonara",
            descrition="ahfjskdl",
            price=123.0,
            category=food,
        )
        url = reverse_lazy("cart_add", args=(prod.pk,))
        code = self.client.post(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_add_to_cart_login_post(self):
        # create cat and product
        food = Category.objects.create(name="food", slug="dinner")
        prod = Product.objects.create(
            name="pasta",
            slug="karbonara",
            description="ahfjskdl",
            price=123.0,
            category=food,
        )

        # create and login user
        url = reverse_lazy("login")
        User.objects.create_user({"username": "user", "password": "pass1234"})
        self.client.post(
            url, {"username": "user", "password": "pass1234"}
        )  # user login

        # making order
        url = reverse_lazy("cart_add", args=(prod.pk,))
        code = self.client.post(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_add_to_cart_wrong_product_id_post(self):
        url = reverse_lazy("cart_add", args=(2221337,))
        code = self.client.post(url).status_code
        self.assertEqual(status.HTTP_404_NOT_FOUND, code)
