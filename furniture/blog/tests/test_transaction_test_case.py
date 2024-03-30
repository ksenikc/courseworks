from unittest import skip
from django.test import TransactionTestCase
from blog.models import Product



class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Product.objects.create(title='Раковина', price=5000)
        Product.objects.create(title='Тумбочка', price=2500)
        self.assertEqual(Product.objects.count(), 2)