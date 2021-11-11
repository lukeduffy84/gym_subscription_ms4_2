import stripe
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from fitness.settings import BASE_URL, STRIPE_API_KEY
from store.models import Product, Customer, Order

DEFAULT_CART = {"items": [], "total": 0}

stripe.api_key = STRIPE_API_KEY


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
    # cart_data["items"] = items_rendered
    return cart_data_rendered


def tag_router(request, tag):
    return redirect(tag.lower())


def home(request):
    return render(request, "home.html")


def register(request, next="home"):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Customer.objects.create(user=user)
            return redirect(next)
        else:
            print(form.errors)
    return render(request, "register.html", context={"form": form})


def fitness(request):
    products = Product.objects.filter(category="ONLINE_COACHING")
    return render(request, "products.html")


def all_products(request):
    products = Product.objects.all()
    context = {"title": "All Products", "products": products}
    return render(request, "products.html", context=context)


def supplements(request):
    products = Product.objects.filter(category="SUPPLEMENTS")
    context = {"title": "Supplements", "products": products}
    return render(request, "products.html", context=context)


def merchandise(request):
    products = Product.objects.filter(category="MERCHANDISE")
    context = {"title": "Merchandise", "products": products}
    return render(request, "products.html", context=context)


def online_coaching(request):
    products = Product.objects.filter(category="ONLINE_COACHING")
    context = {"title": "Online Coaching", "products": products}
    return render(request, "products.html", context=context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {"title": f"{product.category}: {product.name}", "product": product}
    return render(request, "product_detail.html", context=context)


def testimonials(request):
    return render(request, "testimonials.html")


def cart(request):
    cart_data = render_cart(request)
    print(cart_data)
    return render(request, "cart.html", context={"cart_data": cart_data})


def add_to_cart(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product_id"])
        quantity = int(request.POST.get("quantity", 1))
        subtotal = product.price_cents * quantity / 100
        new_item = {
            "product_id": product.id,
            "quantity": quantity,
            "subtotal": subtotal,
        }

        cart = request.session.get("cart", DEFAULT_CART)
        cart["items"].append(new_item)
        cart["total"] += subtotal

        request.session["cart"] = cart

        return redirect("cart")


def update_cart_item(request):
    return redirect("cart")


def remove_cart_item(request, id):
    return redirect("cart")


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


def checkout(request):
    cart_data = render_cart(request)
    stripe_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=stripe_line_items_from_cart_items(cart_data["items"]),
        mode="payment",
        success_url=f'{BASE_URL}{reverse("payment_success")}',
        cancel_url=f'{BASE_URL}{reverse("cart")}',
        shipping_address_collection={
            "allowed_countries": ["US"],
        },
    )
    stripe_session_id = str(stripe_session.id)
    request.session["stripe_session_id"] = stripe_session_id
    return redirect(stripe_session.url, code=303)


def payment_success(request):
    try:
        stripe_session_id = request.session.get("stripe_session_id")
        session = stripe.checkout.Session.retrieve(
            request.session.get("stripe_session_id"),
        )
        print(session)
        if session["payment_status"] == "paid":
            customer = (
                Customer.objects.get(user=request.user)
                if request.user.is_authenticated
                else None
            )
            cart_data = render_cart(request)
            Order.objects.create(
                customer=customer,
                cart_data=cart_data,
                stripe_session_id=stripe_session_id,
                shipping_data=session["shipping"],
            )
            request.session.pop("cart")
            request.session.pop("stripe_session_id")
            return render(request, "success.html")
        else:
            redirect("cart")
    except Exception:
        return redirect("home")


def stripe_webhook(request):
    # TODO: Implement webhook for processing order on payment success.
    pass


def clear_session(request):
    request.session.clear()
    return redirect("home")
