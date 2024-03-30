from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from .views import home, record, ProductDetailView, PostCreateView , UserProductListView, OrderCreateView , UserOrdersListView,ajax_change_status

urlpatterns = [
    path('', home, name="blog-home"),
    path('record/', record, name='record'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('orders/<str:username>', UserOrdersListView.as_view(), name='orders-list'),
    path('orders/new/<int:pk>/', OrderCreateView.as_view(), name='orders-create'),
    path('<int:pk>/update', ajax_change_status, name='ajax_change_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
