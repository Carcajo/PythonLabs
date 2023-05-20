import rest_framework.status as status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from gshop.models import Category, Product


class TestOrders(APITestCase):
    def test_order_create_post(self):
        # create cat and product
        cat = Category.objects.create(name="food", slug="dinner")
        prod = Product.objects.create(
            name="pasta",
            slug="karbonara",
            description="test",
            price=123.0,
            category=cat,
        )

        # create and login user
        url = reverse_lazy("login")
        User.objects.create_user({"username": "user", "password": "pass1234"})
        self.client.post(
            url, {"username": "user", "password": "pass1234"}
        )  # user login

        # add to cart
        url = reverse_lazy("cart_add", args=(prod.pk,))
        self.client.post(url)

        # checkout cart
        url = reverse_lazy("checkout")
        code = self.client.post(
            url,
            {
                "first_name": "pavel",
                "second_name": "glytov",
                "email": "pglutov@gmail.com",
                "address": "myaddress",
                "postal_code": "234792",
                "city": "minsk",
            },
        ).status_code
        self.assertEqual(status.HTTP_200_OK, code)
