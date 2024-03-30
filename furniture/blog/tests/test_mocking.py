from unittest import skip
from django.test import TestCase, RequestFactory
from unittest.mock import Mock, patch
from blog.models import Product
from blog.views import home


class GoogListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_name_list_view(self):
        Product.objects.create(title='Диван', price=10000)
        Product.objects.create(title='Стол', price=1500)

        request = self.factory.get('/home/')

        mock_queryset = Mock(spec=Product.objects.all())
        mock_queryset.return_value = [
            Mock(title='Диван', price=10000),
            Mock(title='Стол', price=1500)
        ]

        with patch('blog.views.Product.objects.all', mock_queryset):
            response = home(request)

        self.assertEqual(response.status_code, 200)


