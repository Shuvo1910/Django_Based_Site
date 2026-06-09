from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfoModel(AbstractUser):
    USER_TYPES = [
        ('Admin','Admin'),
        ('Seller','Seller'),
        ('Customer','Customer'),
    ]

    full_name = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, null=True)

    def __str__(self):
        return f'{self.full_name}'


class ProductModel(models.Model):
    product_name = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='product_img', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_by = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.product_name}'
