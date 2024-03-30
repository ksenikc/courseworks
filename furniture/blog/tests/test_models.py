from unittest import skip
from django.test import TestCase
from blog.models import Product


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Product.objects.create(title="Шкаф", price=12000)

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Шкаф')

    def tearDown(self):
        pass
