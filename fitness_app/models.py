from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, Model

# Create your models here.


class Customer(models.Model):

    email = models.CharField(max_length=500,null=True)
    username = models.CharField(max_length=500,null=True)
    password = models.CharField(max_length=500,null=True)
    created_at=DateTimeField(auto_now_add=True)
    updated_at=DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.id


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.CharField(max_length=500)
    image_link = models.CharField(max_length=500)
    name = models.CharField(max_length=500,null=True)
    has_sizes = models.CharField(max_length=500,null=True)
    rating = models.IntegerField(null=True)
    sku = models.CharField(max_length=500,null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=500,null=True)
    created_at=DateTimeField(auto_now_add=True)
    updated_at=DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.id