from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from blog.models import Product
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NameFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_product_list_functional(self):
        # Create test data
        Product.objects.create(title='Диван', price=10000)
        Product.objects.create(title='Стол', price=1500)

        # Simulate user interactions using Selenium
        self.selenium.get(self.live_server_url)
        self.assertIn('Главная страница', self.selenium.title)
        names = self.selenium.find_elements(By.CLASS_NAME, 'product-item')
        self.assertEqual(len(names), 2)
        self.assertEqual(names[0].text.split('\n')[0], 'Диван')
        self.assertEqual(names[1].text.split('\n')[0], 'Стол')
