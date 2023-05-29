
import rest_framework.status as status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import Product, Category


class TestViewsModels(APITestCase):


    def test_home_get(self):
        url = reverse_lazy('home')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_all_products_get(self):
        url = reverse_lazy('all_products')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_about_get(self):
        url = reverse_lazy('about')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_login_get(self):
        url = reverse_lazy('login')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_logout_get(self):
        url = reverse_lazy('logout')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_register_get(self):
        url = reverse_lazy('register')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_cat_empty_get(self):
        category_slug = "pizza"
        url = reverse_lazy('category', args=(category_slug,))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_404_NOT_FOUND, code)

    def test_product_not_empty_get(self):
        cat = Category.objects.create(name="pizza", slug="pizza")
        prod = Product.objects.create(name="vetchina", slug="vetchina", description="test", price=123.0, category=cat)
        url = reverse_lazy('product', args=(cat.slug, prod.slug))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)


    def test_register_post(self):
        url = reverse_lazy('register')
        code = self.client.post(url, {"username": "ilya", "first_name": "ilya", "last_name": "ilya", "phone_number":
            "+375296465380", "mail": "i.lazuk@bk.ru", "password1": "blablabla"}).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_login_post(self):
        url = reverse_lazy('login')
        User.objects.create_user({"username": "testbro", "password": "blahblahblah"})
        code = self.client.post(url, {"username": "testbro", "password": "blahblahblah"}).status_code
        self.assertEqual(status.HTTP_200_OK, code)





# class TestViewsModel(APITestCase):
#     # create test model objects in db
#
#     #                              category=cat)


