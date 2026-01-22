from django.contrib.auth.models import AbstractUser
from django.db import models


# 1) Admin

class AdminUser(AbstractUser):
    
    admin_key = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.username


# 2) CATEGORY

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


# 3) PRODUCT / MEAL

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products/", default='products/1.png')
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    def __str__(self):
        return self.name


# 7) ORDER 
class Order(models.Model):
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("delivered", "Delivered"),
            ("cancelled", "Cancelled"),
        ],
        default="pending"
    )

    
    products = models.ManyToManyField(
        Product,
        related_name="orders"
    )

    
    confirmed_by = models.ForeignKey(
        AdminUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


