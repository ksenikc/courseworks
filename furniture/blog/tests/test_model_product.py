from django.test import TestCase
from blog.models import Product


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title='Диван',description='Качество на высоте!', price='10000')

    def test_first_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Наименование')

    def test_phone_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Описание')

    def test_surname_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('price').max_length
        self.assertEqual(max_length, 50)
