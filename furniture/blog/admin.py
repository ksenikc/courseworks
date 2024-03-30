from django.contrib import admin
from .models import Product
from .models import Reviews, Stat,Orders

admin.site.register(Product)
admin.site.register(Reviews)

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'stat', 'prod', 'description', 'owner')
    list_display_links = ('id', 'created', 'stat', 'prod', 'description', 'owner')