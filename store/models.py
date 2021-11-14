from django.contrib.auth.models import User
from django.db import models, transaction
from secrets import token_urlsafe


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class OrderManager(models.Manager):
    def create(self, customer, cart_data, stripe_session_id, shipping_data):
        with transaction.atomic():
            order = super().create(
                order_id=token_urlsafe(8),
                customer=customer,
                stripe_session_id=stripe_session_id,
                shipping=shipping_data,
            )
            for item in cart_data["items"]:
                OrderItem.objects.create(
                    order=order, product=item["product"], quantity=item["quantity"]
                )


class Order(models.Model):

    objects = OrderManager()

    class Meta:
        ordering = ["-created"]

    order_id = models.CharField(max_length=15, editable=False, unique=True)
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.CASCADE, null=True
    )
    stripe_session_id = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    shipping = models.JSONField()
    shipped = models.BooleanField(default=False)

    @property
    def total(self):
        return sum([o.quantity * o.product.price_cents for o in self.items.all()])

    @property
    def total_pretty(self):
        return f"${'%.2f' % (self.total/100)}"


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
