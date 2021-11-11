from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.CASCADE
    )

    @property
    def total(self):
        return sum([o.quantity * o.product.price for o in self.items.all()])


class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Product(models.Model):
    def __str__(self):
        return self.name

    SUPPLEMENTS = "SUPPLEMENTS"
    MERCHANDISE = "MERCHANDISE"
    ONLINE_COACHING = "ONLINE_COACHING"
    CATEGORIES = [
        (SUPPLEMENTS, "Supplements"),
        (MERCHANDISE, "Merchandise"),
        (ONLINE_COACHING, "Online Coaching"),
    ]

    name = models.CharField(max_length=100)
    image_url = models.URLField()
    category = models.CharField(max_length=15, choices=CATEGORIES)
    sku = models.CharField(max_length=30)
    price_cents = models.IntegerField()
    description = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def price_whole(self):
        return self.price_cents / 100

    @property
    def price_pretty(self):
        return f"${'%.2f' % self.price_whole}"

    @property
    def category_pretty(self):
        return self.category.replace("_", " ").title()
