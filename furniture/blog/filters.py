import django_filters
from .models import Product


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title')
    price = django_filters.CharFilter(field_name='price')

    class Meta:
        model = Product
        fields = ['title', 'price']