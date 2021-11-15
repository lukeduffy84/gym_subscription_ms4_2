from threading import Thread

import stripe
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from fitness.settings import BASE_URL, STRIPE_API_KEY
from store.cart import (
    render_cart,
    stripe_line_items_from_cart_items,
    current_cart_or_default,
    add_product_to_cart, order_to_cart,
)
from store.models import Product, Customer, Order


stripe.api_key = STRIPE_API_KEY


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


def cart(request):
    cart_data = render_cart(request)
    return render(request, "cart.html", context={"cart_data": cart_data})


def add_to_cart(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product_id"])
        quantity = int(request.POST.get("quantity", 1))
        add_product_to_cart(request, product, quantity)
        return redirect("cart")


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
    stripe_session_id = request.session.get("stripe_session_id")
    session = stripe.checkout.Session.retrieve(
        request.session.get("stripe_session_id"),
    )

    if session["payment_status"] == "paid":
        if request.user.is_authenticated:
            customer, _ = Customer.objects.get_or_create(user=request.user)
        else:
            customer = None

        cart_data = render_cart(request)
        order = Order.objects.create(
            customer=customer,
            cart_data=cart_data,
            stripe_session_id=stripe_session_id,
            stripe_checkout_data=session.to_dict(),
        )
        request.session.pop("cart")
        request.session.pop("stripe_session_id")

        Thread(
            target=lambda: send_mail(
                f"Order confirmed",
                f"Your order #{order.order_id} is confirmed. We'll notify you again once it's on its way.",
                '"Luke Duffy Fitness" <lukeduffyfitness@mail.com>',
                [order.email],
                html_message=render_to_string("email_confirmed.html", {"order": order}),
            )
        ).start()

        return render(request, "success.html")
    else:
        redirect("cart")


def customer_orders(request):
    orders = Order.objects.filter(customer__user=request.user)
    context = {"title": "My Orders", "orders": orders}
    return render(request, "customer_orders.html", context=context)


def order_again(request, pk):
    order = Order.objects.get(id=pk)
    order_to_cart(order, request)
    return redirect("cart")


def stripe_webhook(request):
    # TODO: Implement webhook for processing order on payment success.
    pass


def clear_session(request):
    request.session.clear()
    return redirect("home")
