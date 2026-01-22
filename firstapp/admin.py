from django.contrib import admin
from .models import (
    AdminUser, Category, Product, Order
)

admin.site.register(AdminUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)

