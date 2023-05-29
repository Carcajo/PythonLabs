import rest_framework.status as status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from gshop.models import Product, Category


class TestCart(APITestCase):
    def test_cart_add_no_login_post(self):
        cat = Category.objects.create(name="pizza", slug="pizza")
        prod = Product.objects.create(name="vetchina", slug="vetchina", description="test", price=123.0, category=cat)
        url = reverse_lazy('cart_add', args=(prod.pk,))
        code = self.client.post(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_add_to_cart_login_post(self):
        # create cat and product
        cat = Category.objects.create(name="pizza", slug="pizza")
        prod = Product.objects.create(name="vetchina", slug="vetchina", description="test", price=123.0, category=cat)

        # create and login user
        url = reverse_lazy('login')
        User.objects.create_user({"username": "testbro", "password": "blahblahblah"})
        self.client.post(url, {"username": "testbro", "password": "blahblahblah"})  # user login

        # making order
        url = reverse_lazy('cart_add', args=(prod.pk,))
        code = self.client.post(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_add_to_cart_wrong_product_id_post(self):
        url = reverse_lazy('cart_add', args=(2221337,))
        code = self.client.post(url).status_code
        self.assertEqual(status.HTTP_404_NOT_FOUND, code)
