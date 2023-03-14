from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestListCreateCategory(APITestCase):

    def test_create_category(self):
        cat_dict = {"name": "test"}
        response = self.client.post(reverse('cat_create'), cat_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        prod_dict = {"category": "testcat", "name": "testname", "description": "testdesc", "price": "100"}
        response = self.client.post(reverse('prod_create'), prod_dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        response = self.client.delete('http://127.0.0.1:8000/api/v1/category-delete/', kwargs={'id': 3})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product(self):
        response = self.client.delete('http://127.0.0.1:8000/api/v1/product-delete/', kwargs={'id': 3})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_category(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/category-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/product-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
