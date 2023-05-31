import rest_framework.status as status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from gshop.models import Product, Category


class TestOrders(APITestCase):
    def test_order_create_post(self):
        # create cat and product
        cat = Category.objects.create(name="passenger", slug="passenger")
        prod = Product.objects.create(name="BMW", slug="BMW", description="test", price=123.0, category=cat)

        # create and login user
        url = reverse_lazy('login')
        User.objects.create_user({"username": "testbro", "password": "blahblahblah"})
        self.client.post(url, {"username": "testbro", "password": "blahblahblah"})  # user login

        # add to cart
        url = reverse_lazy('cart_add', args=(prod.pk,))
        self.client.post(url)

        # checkout cart
        url = reverse_lazy('checkout')
        code = self.client.post(url, {"first_name": "artyom", "second_name": "rogachev", "email": "myemail@gmail.com",
                                      "address": "blablabla", "postal_code": "220004", "city": "minsk"}).status_code
        self.assertEqual(status.HTTP_200_OK, code)



