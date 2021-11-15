from store.models import Product

DEFAULT_CART = {"items": [], "total": 0}


def current_cart_or_default(request):
    return request.session.get("cart", DEFAULT_CART)


def add_product_to_cart(request, product, quantity):
    subtotal = product.price_cents * quantity / 100

    new_item = {
        "product_id": product.id,
        "quantity": quantity,
        "subtotal": subtotal,
    }

    cart = current_cart_or_default(request)
    cart["items"].append(new_item)
    cart["total"] += subtotal

    request.session["cart"] = cart


def render_cart(request):
    cart_data = request.session.get("cart", DEFAULT_CART)
    items_rendered = []
    for item in cart_data["items"]:
        product = Product.objects.get(id=item["product_id"])
        items_rendered.append(
            {
                "product": product,
                "quantity": item["quantity"],
                "subtotal": item["subtotal"],
            }
        )
    cart_data_rendered = {"items": items_rendered, "total": cart_data["total"]}
    return cart_data_rendered


def stripe_line_items_from_cart_items(cart_items):
    stripe_items = []
    for item in cart_items:
        stripe_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item["product"].name,
                    },
                    "unit_amount": item["product"].price_cents,
                },
                "quantity": item["quantity"],
            }
        )
    return stripe_items


def order_to_cart(order, request):
    for item in order.items.all():
        add_product_to_cart(request, item.product, item.quantity)
